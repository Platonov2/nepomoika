<template>
  <div>
    <div id="main">
      <router-link to="/AddCategory" class="nav-element">
        <div id="addCategory">
          <div>+ Добавить категорию</div>
        </div>
      </router-link>
      <router-link to="/AddProduct" class="nav-element">
        <div id="addProduct">
          <div>+ Добавить товар</div>
        </div>
      </router-link>
      <div id="parentCategory" v-if="category!=null">
        <div id="back" v-on:click="back(category)">
          &lt; Назад
        </div>
        <div id="categoryName">
          {{ category.category_name }}
        </div>
      </div>
      <ul id="subcategories" v-if="subcategories!=null">
        <div id="subcategories-title">
          Все категории:
        </div>
        <li class="subcategory" v-for="subcategory in subcategories" v-bind:key="subcategory.category_id">
          <div class="subcategoryInfo" v-on:click="changeCategory(subcategory)">
            {{ subcategory.category_name }}
          </div>
          <div class="deleteCategory" v-on:click="deleteCategory(subcategory.category_id)">
            X
          </div>
        </li>
      </ul>
      <ul id="products" v-if="products!=null">
        <li class="product-list" v-for="product in products" v-bind:key="product.product_id">
        <div class="product">
          {{ product.product_name }}
        </div>
       </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../models/Category';

@Component
export default class Home extends Vue {
  get category() {
    return this.$store.getters.CATEGORY;
  }

  get subcategories() {
    return this.$store.getters.SUBCATEGORIES;
  }

  get products() {
    return this.$store.getters.PRODUCTS;
  }

  mounted() {
    this.$store.dispatch('GET_ROOT_CATEGORIES');
  }

  back(category: Category) {
    if (category.root_category_id != null) {
      this.$store.dispatch('CHANGE_CATEGORY', category.root_category_id);
    }
    else {
      this.$store.dispatch('GET_ROOT_CATEGORIES');
    }
  }

  changeCategory(category: Category) {
    this.$store.dispatch('CHANGE_CATEGORY', category);
  }

  deleteCategory(category_id: number) {
    this.$store.dispatch('DELETE_CATEGORY', category_id);
  }
}
</script>

<style lang="scss">
#main {
  display: inline-block;
  width: 100%;
  height: 100%;

  #addCategory {
    display: inline-block;
    margin-left: 20px;
  }

  #addProduct {
    display: inline-block;
    margin-left: 20px;
  }

  #parentCategory {
    display: block;
    margin-top: 20px;
    margin-left: 20px;

    #categoryName, #back {
      display: inline-block;
    }

    #back {
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
    width: 410px;
    margin-left: 20px;
    padding-left: 10px;
    // box-shadow: 1.3px 1.3px 5px #707070;

    #subcategories-title {
      font-size: 16pt;
      padding-top: 10px;
    }

    .subcategory {
      display: flex;
      width: 400px;
      padding: 5px 0px;

      .subcategoryInfo {
        display: inline-block;
        width: 400px;
        font-size: 14pt;
        color: #616060;
        cursor: pointer;
      }

      .subcategoryInfo:hover {
        color: black;
      }

      .deleteCategory {
        display: inline-block;
        color: #616060;
      }

      .deleteCategory:hover {
        color: red;
        cursor: pointer;
      }
    }
  }
}
</style>