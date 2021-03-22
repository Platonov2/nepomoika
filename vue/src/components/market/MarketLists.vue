<template>
  <div>
    <div id="listsWrap">
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
export default class MarketLists extends Vue {
  
}
</script>

<style lang="scss">

#listsWrap {
  display: block;
  margin: 40px 20px;
}


</style>