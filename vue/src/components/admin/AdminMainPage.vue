<template>
  <div>
    <div id="mainWrap">
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
      <AddCategory id="AddCategory"/>
      <AddProduct id="AddProduct"/>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AddCategory from '../AddCategory.vue';
import AddProduct from '../AddProduct.vue';

@Component({
  components: {
    AddCategory,
    AddProduct,
  },
})
export default class AdminMainPage extends Vue {

  mounted() {
    if (this.$store.getters.ADMIN_TOKEN == "") {
      this.$router.push('/admin/login');
    }
  }
}
</script>

<style lang="scss">

#mainWrap {
  margin: 50px;

  #AddCategory {
    margin-right: 70px;
  }
}

</style>