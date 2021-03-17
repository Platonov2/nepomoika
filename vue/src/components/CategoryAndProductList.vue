<template>
  <div>
    <CategoryList id="categoryList"/>
    <ProductList id="productList"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import CategoryList from './CategoryList.vue';
import ProductList from './ProductList.vue';

@Component({
  components: {
    CategoryList,
    ProductList,
  },
})
export default class CategoryAndProductList extends Vue {
  
}
</script>

<style lang="scss">
</style>