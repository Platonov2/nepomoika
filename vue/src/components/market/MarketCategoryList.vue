<template>
  <div>
    <div id="listHeader">
      <div id="currentCategory" >
        <div v-if="category==null">
          <div id="backCursor"></div>
          <div id="categoryName" v-on:click="test()">
            Категории
          </div>
        </div>
        <div v-else id="back">
          <div id="backCursor" v-on:click="back(category)">
            &lt;
          </div>
          <div id="categoryName" v-on:click="back(category)">
            {{ category.category_name }}
          </div>
        </div>
      </div>
    </div>
    <ul id="subcategories" v-if="subcategories!=null">
      <li class="subcategory" v-for="subcategory in subcategories" v-bind:key="subcategory.category_id">
        <div id="subcategoryName">
          <div v-on:click="chooseCategory(subcategory)">
            {{ subcategory.category_name }}
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Category from '../../models/Category';

@Component
export default class MarketCategoryList extends Vue {
  name = "";

  get category() {
    return this.$store.getters.CATEGORY;
  }

  get subcategories() {
    return this.$store.getters.SUBCATEGORIES;
  }

  mounted() {
    this.$store.commit('SET_CATEGORY', null);
    if (this.category == null) {
      this.$store.dispatch('MARKET_GET_ROOT_CATEGORIES');
    }
  }

  test() {
    this.name = "";
    console.log(this.subcategories); 
  }

  back(category: Category) {
    this.$store.commit('SET_PRODUCTS', []);
    if (category.root_category_id != null) {
      this.$store.dispatch('MARKET_CHOOSE_CATEGORY', category.root_category_id);
    }
    else {
      this.$store.dispatch('MARKET_GET_ROOT_CATEGORIES');
    }
    this.$store.commit('SET_EDITED_CATEGORY', {});
    this.$store.commit('SET_EDITED_PRODUCT', {});
  }

  chooseCategory(category: Category) {
    this.$store.dispatch('MARKET_CHOOSE_CATEGORY', category.category_id);
  }
}
</script>

<style lang="scss">

#listHeader {
  
  #currentCategory {
    display: inline-block;
    width: 93%;
    color: rgb(51, 51, 51);

    #backCursor {
      display: inline-block;
      margin-right: 20px;
      font-size: 24pt;
      width: 14px;
      font-weight: bold;
    }

    #backCursor:hover {
      cursor: pointer;
      color: black;
    }

    #categoryName {
      display: inline-block;
      font-size: 24pt;
      font-weight: bold;
    }

    #categoryName:hover {
      cursor: pointer;
      color: black;
    }
  }

  #addCategoryButtonWrap {
    display: inline-block;
    width: 7%;
    text-align: right;

    #addCategoryButton, #rollbackAddingCategory {
      font-size: 24pt;
      margin-right: 10px;
      font-weight: bold;
      color: rgb(51, 51, 51);
    }

    #addCategoryButton:hover, #rollbackAddingCategory:hover {
      color: green;
      cursor: pointer;
    }
  }
}

#subcategories {
  list-style-type: none;
  padding-left: 0px;

  .subcategory {
    display: block;
    width: 500px;
    margin: 5px 0px;
    box-shadow: 2px 2px 5px rgba(122,122,122,0.5);
  }

  #leftPart {
    display: inline-block;
    width: 300px;

    #subcategoryName {
      display: inline-block;
      margin: 5px 0px 5px 15px;
      text-decoration: underline;
      color: #1a1afc;
      font-size: 12pt;
      border: 1px solid white;
    }

    #editName {
      display: inline-block;
      border: 1px solid black;
    }

    #subcategoryName:hover {
      cursor: pointer;
    }
  }
  
  #rightPart {
    display: inline-block;
    width: 200px;
    text-align: right;

    #subcategoryButtons {
      display: inline-block;
      margin-right: 15px;

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