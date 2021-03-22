<template>
  <div>
    <div id="listHeader">
      <div id="currentCategory" >
        <div v-if="category==null">
          <div id="backCursor"></div>
          <div id="categoryName">
            Категории
          </div>
        </div>
        <div v-else id="back">
          <div id="backCursor" v-on:click="back(category)">
            &lt;
          </div>
          <div id="categoryName" v-on:click="back(category)">
            {{ category.category_name }}
          </div>
        </div>
      </div>
      <div id="addCategoryButtonWrap">
        <div id="addCategoryButton" v-if="rootOfNewCategoryId==0"
        v-on:click="showAddCategoryForm(category)">
          +
        </div>
        <div id="rollbackAddingCategory" v-else v-on:click="rollbackAddingCategory()">
          о
        </div>
      </div>
    </div>
    <ul id="subcategories" v-if="subcategories!=null">
      <li class="subcategory" v-for="subcategory in subcategories" v-bind:key="subcategory.category_id">
        <div id="leftPart">
          <div id="subcategoryName">
            <div v-on:click="chooseCategory(subcategory)"
            v-if="subcategory.category_id!=editedCategory.category_id">
              {{ subcategory.category_name }}
            </div>
            <div v-if="subcategory.category_id==editedCategory.category_id">
              <input id="editName" type="text" v-model="name">
            </div>
          </div>
        </div>
        <div id="rightPart">
          <div id="subcategoryButtons">
            <div v-if="subcategory.category_id!=editedCategory.category_id">
              <div v-on:click="editCategory(subcategory)" id="toEdit" class="editButton">
                Р
              </div>
            </div>
            <div v-else>
              <div id="saveChanges" class="editButton" v-on:click="saveChanges()">
                С
              </div>
              <div id="rollbackChanges" class="editButton" v-on:click="rollbackChanges()">
                О
              </div>
              <div id="delete" class="editButton" v-on:click="deleteCategory(subcategory.category_id)">
                У
              </div>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../../models/Category';

@Component
export default class AdminCategoryList extends Vue {
  name = "";

  get category() {
    return this.$store.getters.CATEGORY;
  }

  get rootOfNewCategoryId() {
    return this.$store.getters.ROOT_OF_NEW_CATEGORY_ID;
  }

  get subcategories() {
    return this.$store.getters.SUBCATEGORIES;
  }

  get editedCategory() {
    return this.$store.getters.EDITED_CATEGORY;
  }

  mounted() {
    this.$store.commit('SET_CATEGORY', null);
    if (this.category == null) {
      this.$store.dispatch('ADMIN_GET_ROOT_CATEGORIES');
    }
  }

  back(category: Category) {
    this.$store.commit('SET_PRODUCTS', []);
    if (category.root_category_id != null) {
      this.$store.dispatch('ADMIN_CHOOSE_CATEGORY', category.root_category_id);
    }
    else {
      this.$store.dispatch('ADMIN_GET_ROOT_CATEGORIES');
    }
    this.$store.commit('SET_EDITED_CATEGORY', {});
    this.$store.commit('SET_EDITED_PRODUCT', {});
  }

  showAddCategoryForm(rootCategory: Category) {
    this.$store.commit('SET_ROOT_OF_NEW_PRODUCT_ID', 0);
    this.rollbackAddingCategory();
    if (rootCategory == null){
      this.$store.commit('SET_ROOT_OF_NEW_CATEGORY_ID', -1);
    }
    else {
      this.$store.commit('SET_ROOT_OF_NEW_CATEGORY_ID', rootCategory.category_id);
    }
  }

  rollbackAddingCategory() {
    this.$store.commit('SET_ROOT_OF_NEW_CATEGORY_ID', 0);
  }

  chooseCategory(category: Category) {
    this.$store.dispatch('ADMIN_CHOOSE_CATEGORY', category.category_id);
  }

  editCategory(category: Category) {
    this.$store.commit('SET_EDITED_CATEGORY', category);
    this.name = category.category_name;
  }

  saveChanges() {
    this.editedCategory.category_name = this.name;
    this.$store.dispatch('UPDATE_CATEGORY', this.editedCategory);
    this.$store.commit('SET_EDITED_CATEGORY', {});
    this.rollbackChanges();
  }

  rollbackChanges() {
    this.$store.commit('SET_EDITED_CATEGORY', {});
  }

  deleteCategory(category_id: number) {
    this.$store.dispatch('DELETE_CATEGORY', category_id);
    this.rollbackChanges();
  }
}
</script>

<style lang="scss">

#listHeader {
  
  #currentCategory {
    display: inline-block;
    width: 93%;
    color: rgb(51, 51, 51);

    #backCursor {
      display: inline-block;
      margin-right: 20px;
      font-size: 24pt;
      width: 14px;
      font-weight: bold;
    }

    #backCursor:hover {
      cursor: pointer;
      color: black;
    }

    #categoryName {
      display: inline-block;
      font-size: 24pt;
      font-weight: bold;
    }

    #categoryName:hover {
      cursor: pointer;
      color: black;
    }
  }

  #addCategoryButtonWrap {
    display: inline-block;
    width: 7%;
    text-align: right;

    #addCategoryButton, #rollbackAddingCategory {
      font-size: 24pt;
      margin-right: 10px;
      font-weight: bold;
      color: rgb(51, 51, 51);
    }

    #addCategoryButton:hover, #rollbackAddingCategory:hover {
      color: green;
      cursor: pointer;
    }
  }
}

#subcategories {
  list-style-type: none;
  padding-left: 0px;

  .subcategory {
    display: block;
    width: 500px;
    margin: 5px 0px;
    box-shadow: 2px 2px 5px rgba(122,122,122,0.5);
  }

  #leftPart {
    display: inline-block;
    width: 300px;

    #subcategoryName {
      display: inline-block;
      margin: 5px 0px 5px 15px;
      text-decoration: underline;
      color: #1a1afc;
      font-size: 12pt;
      border: 1px solid white;
    }

    #editName {
      display: inline-block;
      border: 1px solid black;
    }

    #subcategoryName:hover {
      cursor: pointer;
    }
  }
  
  #rightPart {
    display: inline-block;
    width: 200px;
    text-align: right;

    #subcategoryButtons {
      display: inline-block;
      margin-right: 15px;

      .editButton {
        display: inline-block;
        margin-left: 4px;
        color: rgb(51, 51, 51);
        cursor: pointer;
      }

      #toEdit:hover {
        color: black;
      }

      #saveChanges:hover {
        color: green;
      }

      #rollbackChanges:hover {
        color: blue;
      }

      #delete:hover {
        color: red;
      }
    }
  }
}

</style>