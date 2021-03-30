<template>
  <div>
    <div id="wrap">
      <div id="buttons">
        <button id="orders" class="headerButton" v-on:click="onOrderClick()">
          <div id="orders-text">Заказы</div>
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
export default class AdminHeader extends Vue {

  onOrderClick() {
    this.$router.push('/admin/orders');
  }

  onLogoutClick() {
    this.$store.commit('SET_TOKEN', "");
    this.$router.push('/admin/login');
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