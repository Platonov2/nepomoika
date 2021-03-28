<template>
  <div>
    <div id="wrap">
      <div id="buttons">
        <button id="cart" class="headerButton" v-on:click="onCartClick()">
          <div id="cart-text">Корзина</div>
        </button>
        <button id="logout" class="headerButton" v-on:click="onLogoutClick()">
          <div id="logout-text">Выйти</div>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class MarketHeader extends Vue {

  onCartClick() {
    this.$router.push('/cart');
  }

  onLogoutClick() {
    this.$store.commit('SET_TOKEN', "");
    this.$router.push('/authorization');
  }

}
</script>

<style lang="scss">

#wrap {
  display: block;
  height: 100px;
  background-color: burlywood;

  #buttons {
    display: block;
    text-align: right;
    padding-top: 30px;
    padding-right: 50px;
    font-size: 20pt;

    .headerButton {
      width: 100px;
      height: 30px;
      margin-right: 15px;
      cursor: pointer;
    }
  }
}

</style>