<template>
  <div>
    <div id="parentCategory" v-if="category!=null">
      <div id="back" v-on:click="back(category)">
        &lt; Back to
      </div>
      <div id="categoryName">
        {{ category.category_name }}
      </div>
    </div>
    <ul id="subcategories" v-if="subcategories!=null">
      <div id="rootCategoryTitle" v-if="category==null">
        Root categories:
      </div>
      <div id="subcategoriesTitle" v-if="category!=null">
        Subcategories:
      </div>
      <li class="subcategory" v-for="subcategory in subcategories" v-bind:key="subcategory.category_id">
        <div class="subcategoryInfo" v-on:click="chooseCategory(subcategory)"
        v-if="subcategory.category_id!=editedCategory.category_id">
          {{ subcategory.category_name }}
        </div>
        <div class="editedSubcategoryInfo" v-if="subcategory.category_id==editedCategory.category_id">
          <input id="editedName" type="text" v-model="name">
        </div>
        <div id="subcategoryButtons">
          <div id="edit" v-on:click="editCategory(subcategory)"
          v-if="subcategory.category_id!=editedCategory.category_id">
            Редактирование
          </div>
          <div id="onEditModeButtons" v-if="subcategory.category_id==editedCategory.category_id">
            <div id="saveChanges" class="editButton" v-on:click="saveChanges()">
              Сохранить изменения
            </div>
            <div id="rollbackChanges" class="editButton" v-on:click="rollbackChanges()">
              Отменить изменения
            </div>
            <div id="delete" class="editButton" v-on:click="deleteCategory(subcategory.category_id)">
              Удалить
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../models/Category';

@Component
export default class CategoryList extends Vue {
  name = "";

  mounted() {
    if (this.category == null) {
      this.$store.dispatch('GET_ROOT_CATEGORIES');
    }
  }

  get category() {
    return this.$store.getters.CATEGORY;
  }

  get subcategories() {
    return this.$store.getters.SUBCATEGORIES;
  }

  get editedCategory() {
    return this.$store.getters.EDITED_CATEGORY;
  }

  back(category: Category) {
    if (category.root_category_id != null) {
      this.$store.dispatch('SET_CURRENT_CATEGORY', category.root_category_id);
      this.$store.dispatch('CHOOSE_CATEGORY', category.root_category_id);
    }
    else {
      this.$store.dispatch('GET_ROOT_CATEGORIES');
    }
    this.$store.commit('SET_EDITED_CATEGORY', {});
    this.$store.commit('SET_EDITED_PRODUCT', {});
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
#parentCategory {
  display: block;
  margin-top: 20px;
  margin-left: 20px;

  #categoryName{
    display: inline-block;
    margin-left: 10px;
    color: #616060;
    font-size: 16pt;
  }

  #back {
    display: inline-block;
    color: #616060;
    cursor: pointer;
    font-size: 16pt;
  }

  #back:hover {
    color: black;
  }
}

#subcategories {
  display: block;
  margin-left: 20px;
  padding-left: 10px;


  .subcategory {
    display: flex;
    justify-content: space-between;
    width: 80%;
    margin: 10px auto;
    padding: 10px;


    .subcategoryInfo {
      display: inline-block;
      font-size: 14pt;
      color: #616060;
      cursor: pointer;
    }

    .subcategoryInfo:hover {
      color: black;
    }
  }
}

#editCategory, #onEditModeButtons {
  display: inline-block;
  text-align: right;
  margin-right: 10px;
}

#edit:hover {
  color: green;
  cursor: pointer;
}

.editButton {
  display: inline-block;
  margin-left: 10px;
  color: #616060;
}

#saveChanges:hover {
  color: green;
  cursor: pointer;
}

#rollbackChanges:hover {
  color: rgba(0, 4, 255, 0.788);
  cursor: pointer;
}

#delete:hover {
  display: inline-block;
  color: red;
  cursor: pointer;
}
</style>