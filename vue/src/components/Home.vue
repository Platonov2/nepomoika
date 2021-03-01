<template>
  <div>
    Home
    <router-link to="/AddCategory" class="nav-element">
      <div>
        <div>+ Добавить категорию</div>
      </div>
    </router-link>
    <router-link to="/AddProduct" class="nav-element">
      <div>
        <div>+ Добавить товар</div>
      </div>
    </router-link>
    <ul id="root-list">
      Все категории
      <li class="rootCategory-list" v-for="category in rootCategories" v-bind:key="category.category_id">
        <div class="rootCategory" v-on:click="showSubcategories(category)">
          {{ category.category_name }};
        </div>
        <ul v-if="subcategoriesShowed">
          <li class="subCategory-list"
          v-for="subCategory in currentCategories" v-bind:key="subCategory.category_id">
            <div class="subCategory" v-if="subCategory.root_category_id=category.category_id">
              {{ subCategory.category_name }};
            </div>
          </li>
        </ul>
      </li>
    </ul>
    <ul>
      <li class="product-list" v-for="product in currentProducts" v-bind:key="product.product_id">
        <div class="product"
        v-if="product.product_category_id=subCategory.category_id">
          {{ product.product_name }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../models/Category';

@Component
export default class Home extends Vue {
  get rootCategories() {
    return this.$store.getters.ROOT_CATEGORIES;
  }

  get currentCategories() {
    return this.$store.getters.CURRENT_CATEGORIES;
  }

  get currentProducts() {
    return this.$store.getters.CURRENT_PRODUCTS;
  }

  mounted() {
    this.$store.dispatch('GET_ROOT_CATEGORIES');
  }

  showSubcategories(category: Category) {
    this.$store.dispatch('CHANGE_CURRENT_CATEGORY', category);
  }
}
</script>

<style>

</style>