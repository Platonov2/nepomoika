<template>
  <div>
    <div id="addProductWrap">
      <div id="inputs">
        <div id="title">
          Добавление товара
        </div>
        <input class="input"
          v-model.lazy.trim="product.product_name"
          placeholder="Название товара"
        />
        <input class="input"
          v-model.lazy.trim="product.product_price"
          placeholder="Цена товара"
        />
        <input class="input"
          v-model.lazy.trim="product.image_link"
          placeholder="Ссылка на изображение"
        />
        <div id="error">
          {{ error }}
        </div>
        <button id="addProduct" class="input" v-on:click="onAddCategoryClick">
          <div id="addProduct-text">+ Добавить товар</div>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Product from '../../models/Product';

@Component
export default class AdminAddProduct extends Vue {
  product = {} as Product;
  error = "";

  get rootOfNewProductId() {
    return this.$store.getters.ROOT_OF_NEW_PRODUCT_ID;
  }

  onAddCategoryClick() {
    if (typeof(this.product.product_name)=="undefined" ||
        typeof(this.product.product_price)=="undefined" ||
        this.product.product_price < 0 ||
        typeof(this.product.image_link)=="undefined") {
          this.error = "Заполните все поля корректно";
    }
    else {
      this.product.product_category_id = this.rootOfNewProductId;
      this.$store.
        dispatch('POST_NEW_PRODUCT', [this.product])
        .then(() => {
          this.$store.commit('SET_ROOT_OF_NEW_PRODUCT_ID', 0);
        });
    }
  }
}
</script>

<style lang="scss">

#addProductWrap {
  display: inline-block;
  box-shadow: 1.5px 1.5px 6px rgb(100, 100, 100);
  vertical-align: top;
  width: 400px;
  margin-left: 70px;

  #title {
    display: block;
    font-size: 24pt;
    font-weight: bold;
    color: rgb(51, 51, 51);
    padding: 20px 0px;
    margin-bottom: 20px;
  }

  #inputs {
    display: block;
    margin: 20px 40px;
    padding-bottom: 20px;

    .input {
      display: block;
      width: 100%;
      font-size: 14pt;
      margin-bottom: 15px;
    }

    #error {
      display: block;
      margin-top: 10px;
      height: 12pt;
      color: red;
    }

    #addProduct {
      display: block;
      margin-left: 3px;
      padding-bottom: 10px;
      margin-top: 30px;
      cursor: pointer;

      #addProduct-text {
        margin-top: 10px;
      }
    }
  }
}

</style>