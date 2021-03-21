<template>
  <div>
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
export default class MarketCategoryList extends Vue {
  name = "";

  get subcategories() {
    return this.$store.getters.SUBCATEGORIES;
  }

  get editedCategory() {
    return this.$store.getters.EDITED_CATEGORY;
  }

  chooseCategory(category: Category) {
    this.$store.dispatch('SET_CURRENT_CATEGORY', category.category_id);
    this.$store.dispatch('CHOOSE_CATEGORY', category.category_id);
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

#subcategories {
  list-style-type: none;
  padding-left: 26px + 10px;

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