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

</style>