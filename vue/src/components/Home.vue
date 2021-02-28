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
    <ul id="products-list">
      Все категории
      <li class="product" v-for="category in categories" v-bind:key="category.category_id">
        categoryId - {{ category.category_id }};
        category_name - {{ category.category_name }};
        root_category_id - {{ category.root_category_id }};
      </li>
    </ul>
    .
    <ul id="products-list">
      Все товары из первой категории
      <li class="product" v-for="product in currentProducts" v-bind:key="product.product_id">
        product_id - {{ product.product_id }};
        product_name - {{ product.product_name }};
        product_price - {{ product.product_price }};
        image_link - {{ product.image_link }};
        product_category_id - {{ product.product_category_id }};
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Home extends Vue {
  get categories() {
    return this.$store.getters.CATEGORIES;
  }

  get currentProducts() {
    return this.$store.getters.CURRENT_PRODUCTS;
  }

  mounted() {
    this.$store.dispatch('GET_COMPANIES');
    this.$store.dispatch('GET_PRODUCTS_BY_CATEGORY', 1);
  }
}
</script>

<style>

</style>