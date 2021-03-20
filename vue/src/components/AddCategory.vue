<template>
  <div id="AddCategory">
    <div id="inputs">
      <div id="title">
        Добавление категории
      </div>
      <input class="input"
        v-model.lazy.trim="category.category_name"
        placeholder="Название категории"
      />
      <input class="input"
        v-model.lazy.trim="category.root_category_id"
        placeholder="ID родительской категории"
      />
      <div id="error">
        {{ error }}
      </div>
      <button id="addCategory" class="input" v-on:click="onAddCategoryClick">
        <div id="addCategory-text">+ Добавить категорию</div>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../models/Category';

@Component
export default class AddCategory extends Vue {
  category = {} as Category;
  error = "";

  onAddCategoryClick() {
    if (typeof(this.category.category_name)=="undefined" ||
          typeof(this.category.root_category_id)=="undefined") {
            this.error = "Заполните все поля корректно";
      }
      else {
        this.$store.
          dispatch('POST_NEW_CATEGORY', [this.category])
          .then(() => {
            this.$router.push('/');
            this.$store.dispatch('SET_CURRENT_CATEGORY', this.category.root_category_id);
            this.$store.dispatch('CHOOSE_CATEGORY', this.category.root_category_id);
          });
      }
  }
}
</script>

<style lang="scss">

#AddCategory {
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

    #addCategory {
      display: block;
      margin-left: 3px;
      padding-bottom: 10px;
      margin-top: 30px;
      cursor: pointer;

      #addCategory-text {
        margin-top: 10px;
      }
    }
  }
}

</style>