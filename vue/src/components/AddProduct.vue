<template>
  <div id="AddProduct">
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
      <input class="input"
        v-model.lazy.trim="product.product_category_id"
        placeholder="ID родительской категории"
      />
      <div id="error">
        {{ error }}
      </div>
      <button id="addProduct" class="input" v-on:click="onAddCategoryClick">
        <div id="addProduct-text">+ Добавить товар</div>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Product from '../models/Product';

@Component
export default class AddProduct extends Vue {
    product = {} as Product;
    error = "";

    onAddCategoryClick() {
      if (typeof(this.product.product_name)=="undefined" ||
          typeof(this.product.product_price)=="undefined" ||
          this.product.product_price < 0 ||
          typeof(this.product.image_link)=="undefined" ||
          typeof(this.product.product_category_id)=="undefined") {
            this.error = "Заполните все поля корректно";
      }
      else {
        this.$store.
          dispatch('POST_NEW_PRODUCT', [this.product])
          .then(() => {
            this.$router.push('/');
            this.$store.dispatch('SET_CURRENT_CATEGORY', this.product.product_category_id);
            this.$store.dispatch('CHOOSE_CATEGORY', this.product.product_category_id);
          });
      }
  }
}
</script>

<style lang="scss">

#AddProduct {
  display: inline-block;
  box-shadow: 1.5px 1.5px 6px rgb(100, 100, 100);
  vertical-align: top;
  width: 400px;

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