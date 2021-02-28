<template>
  <div id="AddCategory">
    AddCategory
    <input
      v-model.lazy.trim="category.category_name"
      placeholder="Название категории"
    />
    <input
      v-model.lazy.trim="category.root_category_id"
      placeholder="ID родительской категории"
    />
    <button id="addCompanyButton-layout" v-on:click="onAddCategoryClick">
      <div id="addCompanyButton-text">+ Добавить категорию</div>
    </button>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../models/Category';

@Component
export default class AddCategory extends Vue {
  category = {} as Category;

  onAddCategoryClick() {
    this.$store.
      dispatch('POST_NEW_CATEGORY', [this.category])
      .then(() => {
        this.$router.push('/');
      });
  }
}
</script>

<style>

</style>