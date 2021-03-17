<template>
  <div>
    <ul id="products" v-if="products!=null">
      <div class="category-title" id="products-title">
        Products in category:
      </div>
      <li class="product-list" v-for="product in products" v-bind:key="product.product_id">
        <div class="product">
          <div class="productFields" v-if="product.product_id!=editedProduct.product_id">
            <div class="productField">
              Name: {{ product.product_name }}
            </div>
            <div class="productField">
              Price: {{ product.product_price }}
            </div>
          </div>
          <div class="editedProductInfo" v-if="product.product_id==editedProduct.product_id">
            <input class="productField" type="text" v-model="name">
            <input class="productField" type="text" v-model="price">
          </div>
          <div id="productButtons">
            <div id="edit" v-on:click="editProduct(product)"
            v-if="product.product_id!=editedProduct.product_id">
              Редактирование
            </div>
            <div id="onEditModeButtons" v-if="product.product_id==editedProduct.product_id">
              <div id="saveChanges" class="editButton" v-on:click="saveChanges()">
                Сохранить изменения
              </div>
              <div id="rollbackChanges" class="editButton" v-on:click="rollbackChanges()">
                Отменить изменения
              </div>
              <div id="delete" class="editButton" v-on:click="deleteProduct(product.product_id)">
                Удалить
              </div>
            </div>
          </div>
          <!-- <image src= "{{ product.image_link }}" alt="not succ"/> -->
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Product from '../models/Product';

@Component
export default class ProductList extends Vue {
  name = "";
  price = 0;
  imageLink = "";

  get products() {
    return this.$store.getters.PRODUCTS;
  }

  get editedProduct() {
    return this.$store.getters.EDITED_PRODUCT;
  }

  editProduct(product: Product) {
    this.$store.commit('SET_EDITED_PRODUCT', product);
    this.name = product.product_name;
    this.price = product.product_price;
    this.imageLink = product.image_link;
  }

  saveChanges() {
    this.editedProduct.product_name = this.name;
    this.editedProduct.product_price = this.price;
    this.$store.dispatch('UPDATE_PRODUCT', this.editedProduct);
    this.$store.commit('SET_EDITED_PRODUCT', {});
    this.rollbackChanges();
  }

  rollbackChanges() {
    this.$store.commit('SET_EDITED_PRODUCT', {});
  }

  deleteProduct(product_id: number) {
    this.$store.dispatch('DELETE_PRODUCT', product_id);
    this.rollbackChanges();
  }
}
</script>

<style lang="scss">

.product {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  width: 80%;
  margin: 10px auto;
  border-top: 1px solid black;
  border-bottom: 1px solid black;

  .productFields {
    display: inline-block;
  }

  .productField {
    display: block;
    margin: 5px 0px;
  }
}

#products {
  margin-left: 20px;
  padding-left: 10px;
  list-style-type: none;
}

#editProduct, #onEditModeButtons {
  display: inline-block;
  text-align: right;
  margin-right: 10px;
}
</style>