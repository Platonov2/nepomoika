<template>
  <div>
    <div id="listsWrap">
      <AdminCategoryList id="adminCategoryList"/>
      <AdminProductList id="adminProductList"/>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AdminCategoryList from './AdminCategoryList.vue';
import AdminProductList from './AdminProductList.vue';

@Component({
  components: {
    AdminCategoryList,
    AdminProductList,
  },
})
export default class AdminLists extends Vue {
  
}
</script>

<style lang="scss">

#listsWrap {
  display: block;
  margin: 40px 20px;
}


</style>