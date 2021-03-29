<template>
  <div>
    <ul id="cartList">
      <div id="title">
        Текущие заказы
      </div>
      <li class="order" v-for="order in orders" v-bind:key="order.aggregate_id">
        <div id="orderFields">
          <div class="orderField">
            {{ order.aggregate_id }}
          </div>
          <div class="orderField">
            <li class="order" v-for="orderProduct in order.order_products" v-bind:key="orderProduct.product_id">
              {{ orderProduct.product_name }}
            </li>
          </div>
          <div class="orderField">
            {{ order.order_sum }}
          </div>
          <div id="status">
            <div v-if="order.order_status=='OrderStatus.UNCHECKED'">
              На ожидании
            </div>
            <div v-if="order.order_status=='OrderStatus.CANCELED'">
              Отменён
            </div>
          </div>
        </div>
        <div id="buttons">
        <button id="removeProduct" v-on:click="removeOrder(order)">
          Убрать
        </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class MarketOrders extends Vue {

  get orders() {
    return this.$store.getters.ORDERS;
  }

  mounted() {
    this.$store.dispatch("GET_ORDERS");
  }

  removeOrder(order) {
    order.order_status = "OrderStatus.CANCELED";
    this.$store.dispatch("CANCEL_ORDER", order.aggregate_id);
  }
}
</script>

<style lang="scss">

</style>