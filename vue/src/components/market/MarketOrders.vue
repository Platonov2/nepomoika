<template>
  <div>
    <MarketHeader id="marketHeader"/>
    <ul id="ordersList">
      <div id="title">
        Текущие заказы
      </div>
      <li class="order" v-for="order in orders" v-bind:key="order.aggregate_id">
        <div id="orderFields">
          <div id="orderId" class="orderField">
            ID заказа: {{ order.aggregate_id }}
          </div>
          <div id="status">
            <div v-if="order.order_status=='OrderStatus.UNCHECKED'">
              Статус: На ожидании
            </div>
            <div v-if="order.order_status=='OrderStatus.CHECKED'">
              Статус: Выполняется
            </div>
            <div v-if="order.order_status=='OrderStatus.CANCELED'">
              Статус: Отменён
            </div>
            <div v-if="order.order_status=='OrderStatus.COMPLETED'">
              Статус: Завершён
            </div>
            <div v-if="order.order_status=='OrderStatus.ABORTED'">
              Статус: Прерван
            </div>
          </div>
          <div class="orderField">
            <div id="productsTitle">
              Товары:
            </div>
            <li class="orderProduct" v-for="orderProduct in order.order_products" v-bind:key="orderProduct.product_id">
              {{ orderProduct.product_name }}
            </li>
          </div>
          <div id="orderSumm" class="orderField">
            Сумма: {{ order.order_sum }}
          </div>
        </div>
        <div id="buttons">
        <button id="removeProduct" v-on:click="removeOrder(order)"
        v-if="order.order_status=='OrderStatus.UNCHECKED'">
          Отменить
        </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import MarketHeader from './MarketHeader.vue';

@Component({
  components: {
    MarketHeader,
  },
})
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

#ordersList {
  display: block;
  list-style-type: none;
  margin: 40px;

  #title {
    display: block;
    font-size: 18pt;
    font-weight: bold;
    margin: 40px 0px 15px 0px;
  }

  .order {
    display: block;
    width: 500px;
    margin: 5px 0px;
    box-shadow: 2px 2px 5px rgba(122,122,122,0.5);

    #orderFields {
      display: inline-block;
      margin: 5px 0px 5px 15px;
      font-size: 14pt;
      border: 1px solid white;
      width: 350px;

      #orderId, #status {
        display: inline-block;
        width: 50%;
      }

      #status {
        text-align: right;
      }

      #productsTitle {
        padding-top: 5px;
        font-weight: bold;
      }
      
      #orderSumm {
        padding-top: 5px;
      }

      .orderField {
        margin: 5px 0px;
      }
    }

    #buttons {
      display: inline-block;
      vertical-align: bottom;
      margin-bottom: 10px;

      #removeProduct {
        font-size: 12pt;
        width: 100%;
      }
    }
  }
}

</style>