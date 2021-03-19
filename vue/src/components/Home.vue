<template>
  <div>
    <div id="main">
      <div class="buttons">
        <router-link to="/AddCategory" class="nav-element">
          <div id="addCategory">
            <div>+ Добавить категорию</div>
          </div>
        </router-link>
        <router-link to="/AddProduct" class="nav-element">
          <div id="addProduct">
            <div>+ Добавить товар</div>
          </div>
        </router-link>
      </div>
      <CategoryAndProductList id="categoryAndProductList"/>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import CategoryAndProductList from './CategoryAndProductList.vue'

@Component({
  components: {
    CategoryAndProductList,
  },
})
export default class Home extends Vue {
}
</script>

<style lang="scss">

#main {
  display: inline-block;
  margin: 40px;
  width: 90%;
}

#categoryAndProductList {
  display: block;
  margin-top: 20px;
}

</style>