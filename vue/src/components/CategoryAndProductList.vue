<template>
  <div>
    <div id="currentCategory" >
      <div v-if="category==null">
        <div id="backCursor"></div>
        <div id="categoryName">
          Категории
        </div>
      </div>
      <div v-else id="back" v-on:click="back(category)">
        <div id="backCursor">
          &lt;
        </div>
        <div id="categoryName">
          {{ category.category_name }}
        </div>
      </div>
    </div>
    <CategoryList id="categoryList"/>
    <ProductList id="productList"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../models/Category';
import CategoryList from './CategoryList.vue';
import ProductList from './ProductList.vue';

@Component({
  components: {
    CategoryList,
    ProductList,
  },
})
export default class CategoryAndProductList extends Vue {
  get category() {
    return this.$store.getters.CATEGORY;
  }

  mounted() {
    this.$store.commit('SET_CATEGORY', null);
    if (this.category == null) {
      this.$store.dispatch('GET_ROOT_CATEGORIES');
    }
  }

  back(category: Category) {
    this.$store.commit('SET_PRODUCTS', []);
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
}
</script>

<style lang="scss">

#currentCategory {
  color: rgb(51, 51, 51);

  #backCursor {
    display: inline-block;
    margin-right: 20px;
    font-size: 26pt;
    width: 14px;
    font-weight: bold;
  }

  #back:hover {
    cursor: pointer;
    color: black;
  }

  #categoryName {
    display: inline-block;
    font-size: 28pt;
    font-weight: bold;
  }
}
</style>