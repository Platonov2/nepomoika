<template>
  <div>
    <div id="wrap">
      <div id="leftPart">
        <button id="catalog" class="headerButton" v-on:click="onCatalogClick()">
          <div id="catalog-text">Каталог</div>
        </button>
      </div>
      <div id="rightPart">
        <div id="buttons">
          <button id="orders" class="headerButton" v-on:click="onOrderClick()">
            <div id="orders-text">Заказы</div>
          </button>
          <button id="cart" class="headerButton" v-on:click="onCartClick()">
            <div id="cart-text">Корзина</div>
          </button>
          <button id="logout" class="headerButton" v-on:click="onLogoutClick()">
            <div id="logout-text">Выйти</div>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class MarketHeader extends Vue {

  onCatalogClick() {
    this.$router.push('/');
  }

  onOrderClick() {
    this.$router.push('/orders');
  }

  onCartClick() {
    this.$router.push('/cart');
  }

  onLogoutClick() {
    this.$store.commit('DELETE_COOKIE');
    this.$router.push('/authorization');
  }

}
</script>

<style lang="scss">

#wrap {
  display: block;
  height: 100px;
  background-color: burlywood;

  #leftPart {
    display: inline-block;
    width: 15%;

    #catalog {
      display: inline-block;
      margin-top: 30px;
      margin-left: 50px;
    }
  }

  .headerButton {
    display: inline-block;
    width: 100px;
    height: 30px;
    margin-right: 15px;
    cursor: pointer;
  }
  #rightPart {
    display: inline-block;
    width: 85%;
    text-align: right;

    #buttons {
      display: inline-block;
      text-align: right;
      padding-top: 30px;
      padding-right: 50px;
      font-size: 20pt;
    }
  }
}

</style>