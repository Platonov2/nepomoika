<template>
  <div>
    <ul id="products-list">
      <li class="product" v-for="product in products" v-bind:key="product.productId">
        productId - {{ product.productId }}
        categoryId - {{ product.categoryId }}
        price - {{ product.price }}
        name - {{ product.name }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Deals extends Vue {
  get products() {
    return this.$store.getters.PRODUCTS
  }

  mounted() {
    this.$store.dispatch('GET_PRODUCTS');
  }
}

</script>

<style lang="scss">
</style>
