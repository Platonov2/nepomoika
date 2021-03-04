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
      {{ category.category_name }}
      Все категории
      <li class="rootCategory-list" v-for="subcategory in subcategories" v-bind:key="subcategory.category_id">
        <div class="rootCategory" v-on:click="changeCategory(subcategory)">
          {{ subcategory.category_name }};
        </div>
      </li>
    </ul>
    <ul>
      <li class="product-list" v-for="product in products" v-bind:key="product.product_id">
        <div class="product">
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
  get category() {
    return this.$store.getters.CATEGORY;
  }

  get subcategories() {
    return this.$store.getters.CATEGORIES;
  }

  get products() {
    return this.$store.getters.PRODUCTS;
  }

  mounted() {
    this.$store.dispatch('GET_ROOT_CATEGORIES');
  }

  changeCategory(category: Category) {
    this.$store.dispatch('CHANGE_CATEGORY', category);
  }
}
</script>

<style>

</style>