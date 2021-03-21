<template>
  <div>
    <div id="listsWrap">
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
      <MarketCategoryList id="marketCategoryList"/>
      <MarketProductList id="marketProductList"/>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import MarketCategoryList from './MarketCategoryList.vue';
import MarketProductList from './MarketProductList.vue';

@Component({
  components: {
    MarketCategoryList,
    MarketProductList,
  },
})
export default class AdminLists extends Vue {

}
</script>

<style lang="scss">

#listsWrap {
  display: block;
  margin-top: 20px;

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
}


</style>