<template>
  <div>
    <div>
      <AdminHeader id="adminHeader"/>
      <div id="main">
        <AdminLists id="adminLists"/>
        <div id="addingForms">
          <AdminAddCategory id="adminAddCategory" v-if="rootOfNewCategoryId!=0" />
          <AdminAddProduct id="adminAddProduct" v-if="rootOfNewProductId!=0" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AdminHeader from './AdminHeader.vue';
import AdminLists from './AdminLists.vue';
import AdminAddCategory from './AdminAddCategory.vue';
import AdminAddProduct from './AdminAddProduct.vue';

@Component({
  components: {
    AdminHeader,
    AdminLists,
    AdminAddCategory,
    AdminAddProduct,
  },
})
export default class AdminMainPage extends Vue {

  get rootOfNewCategoryId() {
    return this.$store.getters.ROOT_OF_NEW_CATEGORY_ID;
  }

  get rootOfNewProductId() {
    return this.$store.getters.ROOT_OF_NEW_PRODUCT_ID;
  }

  mounted() {
    if (this.$store.getters.TOKEN == "") {
      this.$router.push('/admin/login');
    }
  }
}
</script>

<style lang="scss">

#main {
  margin: 50px;
  height: 100%;

  #adminLists {
    display: inline-block;
    vertical-align: top;
    box-shadow: 2px 2px 5px rgba(122,122,122,0.5);
    width: 540px;
  }

  #addingForms {
    display: inline-block;
  }
}

</style>