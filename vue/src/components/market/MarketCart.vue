<template>
  <div>
    <div>
      <MarketHeader id="marketHeader"/>
      <ul id="cartList">
        <div id="title">
          Товары в корзине
        </div>
        <li class="product" v-for="product in cartProducts" v-bind:key="product.product_id">
          <div id="productFields">
            <div class="productField">
              {{ product.product_name }}
            </div>
            <div class="productField">
              {{ product.product_price }} Р
            </div>
            </div>
          <div id="buttons">
          <button id="removeProduct" v-on:click="removeProduct(product.product_id)">
            Убрать
          </button>
          </div>
        </li>
      </ul>
    </div>
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
export default class MarketCart extends Vue {

  get cartProducts() {
    return this.$store.getters.CART_PRODUCTS;
  }

  mounted() {
    this.$store.dispatch("GET_CART_PRODUCTS");
  }

  removeProduct(product_id: number) {
    this.$store.dispatch("DELETE_CART_PRODUCT", product_id);
  }
}
</script>

<style lang="scss">

#cartList {
  list-style-type: none;
  padding-left: 0px;

  #title {
    display: block;
    font-size: 18pt;
    font-weight: bold;
    margin: 40px 0px 15px 0px;
  }

  .product {
    display: block;
    width: 500px;
    margin: 5px 0px;
    box-shadow: 2px 2px 5px rgba(122,122,122,0.5);

    #productFields {
      display: inline-block;
      margin: 5px 0px 5px 15px;
      font-size: 14pt;
      border: 1px solid white;
      width: 400px;

      .productField {
        margin: 5px 0px;
      }
    }

    #buttons {
      display: inline-block;
      vertical-align: bottom;
      margin-bottom: 10px;

      #addToCart {
        font-size: 12pt;
      }
    }
  }
}

</style>