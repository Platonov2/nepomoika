<template>
  <div>
    <ul id="products" v-if="products[0]!=null">
      <div id="title">
        Товары в категории
      </div>
      <li class="product" v-for="product in products" v-bind:key="product.product_id">
        <div id="productFields">
          <div class="productField">
            {{ product.product_name }}
          </div>
          <div class="productField">
            {{ product.product_price }} Р
          </div>
        </div>
        <div id="buttons">
          <button id="addToCart" v-on:click="addToCart(product)">
            Купить
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class MarketProductList extends Vue {

  get products() {
    return this.$store.getters.PRODUCTS;
  }
}
</script>

<style lang="scss">

#products {
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