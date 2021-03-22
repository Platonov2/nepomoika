<template>
  <div>
    <ul id="products">
      <div id="listHeader">
        <div id="headerText">
          Товары в категории
        </div>
        <div id="addProductButtonWrap">
          <div id="addProductButton" v-if="rootOfNewProductId==0"
          v-on:click="showAddProductForm(category)">
            +
          </div>
          <div id="rollbackAddingProduct" v-else v-on:click="rollbackAddingProduct()">
            о
          </div>
        </div>
      </div>
      <div v-if="products[0]!=null">
        <li class="product" v-for="product in products" v-bind:key="product.product_id">
          <div id="leftPart">
            <div id="productFields" v-if="product.product_id!=editedProduct.product_id">
              <div class="productField">
                {{ product.product_name }}
              </div>
              <div class="productField">
                {{ product.product_price }} Р
              </div>
            </div>
            <div id="editProductInfo" v-else>
              <input class="editField" type="text" v-model="name">
              <input class="editField" type="text" v-model="price">
            </div>
          </div>
          <div id="rightPart">
            <div id="productButtons">
              <div id="toEdit" class="editButton" v-on:click="editProduct(product)"
              v-if="product.product_id!=editedProduct.product_id">
                Р
              </div>
              <div v-else>
                <div id="saveChanges" class="editButton" v-on:click="saveChanges()">
                  С
                </div>
                <div id="rollbackChanges" class="editButton" v-on:click="rollbackChanges()">
                  О
                </div>
                <div id="delete" class="editButton" v-on:click="deleteProduct(product.product_id)">
                  У
                </div>
              </div>
            </div>
            <!-- <image src= "{{ product.image_link }}" alt="not succ"/> -->
          </div>
        </li>
      </div>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../../models/Category';
import Product from '../../models/Product';

@Component
export default class AdminProductList extends Vue {
  name = "";
  price = 0;
  imageLink = "";

  get category() {
    return this.$store.getters.CATEGORY;
  }

  get products() {
    return this.$store.getters.PRODUCTS;
  }

  get editedProduct() {
    return this.$store.getters.EDITED_PRODUCT;
  }

  get rootOfNewProductId() {
    return this.$store.getters.ROOT_OF_NEW_PRODUCT_ID;
  }

  showAddProductForm(rootCategory: Category) {
    this.$store.commit('SET_ROOT_OF_NEW_CATEGORY_ID', 0);
    this.rollbackChanges();
    if (rootCategory == null){
      this.$store.commit('SET_ROOT_OF_NEW_PRODUCT_ID', -1);
    }
    else {
      this.$store.commit('SET_ROOT_OF_NEW_PRODUCT_ID', rootCategory.category_id);
    }
  }

  rollbackAddingProduct() {
    this.$store.commit('SET_ROOT_OF_NEW_PRODUCT_ID', 0);
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

#listHeader {
  
  #headerText {
    display: inline-block;
    font-size: 18pt;
    font-weight: bold;
    width: 93%;
    margin: 40px 0px 15px 0px;
  }

  #addProductButtonWrap {
    display: inline-block;
    width: 7%;
    text-align: right;

    #addProductButton, #rollbackAddingProduct {
      font-size: 24pt;
      margin-right: 10px;
      font-weight: bold;
      color: rgb(51, 51, 51);
    }

    #addProductButton:hover, #rollbackAddingProduct:hover {
      color: green;
      cursor: pointer;
    }
  }
}


#products {
  list-style-type: none;
  padding-left: 0px;

  .product {
    display: inline-block;
    width: 500px;
    margin: 5px 0px;
    box-shadow: 2px 2px 5px rgba(122,122,122,0.5);
  }

  #leftPart {
    display: inline-block;
    width: 300px;

    #productFields {
      display: inline-block;
      margin: 5px 0px 5px 15px;
      font-size: 12pt;
      border: 1px solid white;

      .productField {
        margin: 5px 0px;
      }
    }

    .editField {
      display: inline-block;
      border: 1px solid black;
      margin: 5px 0px 5px 15px;
      font-size: 10pt;
    }

    #subcategoryName:hover {
      cursor: pointer;
    }
  }
  
  #rightPart {
    display: inline-block;
    vertical-align: top;

    display: inline-block;
    width: 200px;
    text-align: right;

    #productButtons {
      display: inline-block;
      margin: 10px 15px 0px 0px;

      .editButton {
        display: inline-block;
        margin-left: 4px;
        color: rgb(51, 51, 51);
        cursor: pointer;
      }

      #toEdit:hover {
        color: black;
      }

      #saveChanges:hover {
        color: green;
      }

      #rollbackChanges:hover {
        color: blue;
      }

      #delete:hover {
        color: red;
      }
    }
  }
}

</style>