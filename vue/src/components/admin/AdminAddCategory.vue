<template>
  <div>
    <div id="addCategoryWrap">
      <div id="inputs">
        <div id="title">
          Добавление категории
        </div>
        <input class="input"
          v-model.lazy.trim="category.category_name"
          placeholder="Название категории"
        />
        <div id="error">
          {{ error }}
        </div>
        <button id="addCategory" class="input" v-on:click="onAddCategoryClick">
          <div id="addCategory-text">+ Добавить категорию</div>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../../models/Category';

@Component
export default class AdminAddCategory extends Vue {
  category = {} as Category;
  error = "";

  get rootOfNewCategoryId() {
    return this.$store.getters.ROOT_OF_NEW_CATEGORY_ID;
  }

  onAddCategoryClick() {
    if (typeof(this.category.category_name)=="undefined") {
            this.error = "Заполните все поля корректно";
      }
      else {
        this.category.root_category_id = this.rootOfNewCategoryId;
        this.$store.
          dispatch('POST_NEW_CATEGORY', [this.category])
          .then(() => {
            this.$store.commit('SET_ROOT_OF_NEW_CATEGORY_ID', 0);
          });
      }
  }
}
</script>

<style lang="scss">

#addCategoryWrap {
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