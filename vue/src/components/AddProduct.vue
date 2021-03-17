<template>
  <div id="AddProduct">
    AddProduct
    <input
      v-model.lazy.trim="product.product_name"
      placeholder="Название товара"
    />
    <input
      v-model.lazy.trim="product.product_price"
      placeholder="Цена товара"
    />
    <input
      v-model.lazy.trim="product.image_link"
      placeholder="Ссылка на изображение"
    />
    <input
      v-model.lazy.trim="product.product_category_id"
      placeholder="ID родительской категории"
    />
    <button id="addCompanyButton-layout" v-on:click="onAddCategoryClick">
      <div id="addCompanyButton-text">+ Добавить товар</div>
    </button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Product from '../models/Product';

@Component
export default class AddProduct extends Vue {
    product = {} as Product;

    onAddCategoryClick() {
    this.$store.
      dispatch('POST_NEW_PRODUCT', [this.product])
      .then(() => {
        this.$router.push('/');
        this.$store.dispatch('SET_CURRENT_CATEGORY', this.product.product_category_id);
        this.$store.dispatch('CHOOSE_CATEGORY', this.product.product_category_id);
      });
  }
}
</script>

<style>

</style>