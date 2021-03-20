<template>
  <div>
    <div id="main">
      <div id="header">
        <div id="buttons">
          <!-- <router-link to="/AddCategory" class="nav-element">
            <div id="addCategory">
              <div>+ Добавить категорию</div>
            </div>
          </router-link>
          <router-link to="/AddProduct" class="nav-element">
            <div id="addProduct">
              <div>+ Добавить товар</div>
            </div>
          </router-link> -->
        </div>
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
  width: 100%;
  padding: 0px;
  margin: 0px;

  #header {
    display: block;
    width: 100%;
    height: 100px;
    background-color: chartreuse;

    #buttons {
      display: block;
    }
  }

  #categoryAndProductList {
    display: block;
    margin: 40px;
    // margin-top: 20px;
    width: 90%;
  }
}


</style>