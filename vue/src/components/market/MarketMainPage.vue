<template>
  <div>
    <div id="main">
      <MarketHeader id="marketHeader"/>
      <MarketLists id="marketLists"/>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import MarketHeader from './MarketHeader.vue';
import MarketLists from './MarketLists.vue';

@Component({
  components: {
    MarketHeader,
    MarketLists,
  },
})
export default class AdminMainPage extends Vue {
}
</script>

<style lang="scss">

#marketLists {
  display: inline-block;
  vertical-align: top;
  margin: 40px 20px;
  margin-left: calc(50% - 270px);
  box-shadow: 2px 2px 5px rgba(122,122,122,0.5);
  width: 540px;
}

</style>