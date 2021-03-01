import Product from '@/models/Product'
import Vuex from 'vuex'
import axios from 'axios'
import Category from '@/models/Category'

export default new Vuex.Store({
  state: {
    rootCategories: [] as Category[],
    currentCategories: [] as Category[],
    currentCategory: {} as Category,
    currentProducts: [] as Product[],
    currentProduct: {} as Product,
  },
  getters: {
    ROOT_CATEGORIES: (state) => state.rootCategories,
    CURRENT_CATEGORIES: (state) => state.currentCategories,
    CURRENT_CATEGORY: (state) => state.currentCategory,
    CURRENT_PRODUCTS: (state) => state.currentProducts,
    CURRENT_PRODUCT: (state) => state.currentProduct,
  },
  mutations: {
    SET_ROOT_CATEGORIES: (state, rootCategories) => {
      state.rootCategories = rootCategories;
    },
    SET_CURRENT_CATEGORIES: (state, currentCategories) => {
      state.currentCategories = currentCategories;
    },
    SET_CURRENT_CATEGORY: (state, currentCategory) => {
      state.currentCategory = currentCategory;
    },
    SET_CURRENT_PRODUCTS: (state, products) => {
      state.currentProducts = products;
    },
    SET_CURRENT_PRODUCT: (state, product) => {
      state.currentProduct = product;
    },
  },
  actions: {
    /**       КАТЕГОРИИ          */

    // Получение списка всех категорий
    GET_ROOT_CATEGORIES: (context) => {
      axios
        .get('http://localhost:8090/category/roots')
        .then((response) => {
          context.commit('SET_ROOT_CATEGORIES', response.data)
        });
    },
    CHANGE_CURRENT_CATEGORY: (context, category: Category) => {
      axios
        .get('http://localhost:8090/category/children', {
          params: category.category_id,
        })
        .then((response) => {
          context.commit('SET_CURRENT_CATEGORY', category);
          context.commit('SET_CURRENT_CATEGORIES', response.data);
        });
    },
    // Добавление новой категории
    POST_NEW_CATEGORY(state, category: Category) {
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8090/category', category)
          .then((response) => {
            console.log(response);
          });
      });
    },
    // Обновление категории
    UPDATE_CATEGORY(state, category: Category) {
      return new Promise((resolve, reject) => {
        axios
          .put('http://localhost:8090/category', category)
          .then((response) => {
            console.log(response);
          });
      });
    },
    // Удаление категории
    DELETE_CATEGORY(state, category_id: number) {
      return new Promise((resolve, reject) => {
        axios
          .delete('http://localhost:8090/category', {
            params: category_id,
          })
          .then((response) => {
            console.log(response);
          });
      });
    },

    /**       ТОВАРЫ          */

    // Получение товара по его id
    GET_PRODUCT: (context, product_id: number) => {
      axios
        .get('http://localhost:8090/product', {
          params: product_id,
        })
        .then((response) => {
          context.commit('SET_CURRENT_PRODUCT', response.data)
        });
    },
    // Получение всех товаров из категории по его id
    GET_PRODUCTS_BY_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/product', {
          params: category_id,
        })
        .then((response) => {
          context.commit('SET_CURRENT_PRODUCTS', response.data)
        });
    },
    // Добавление нового товара
    POST_NEW_PRODUCT(state, product: Product) {
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8090/product', product)
          .then((response) => {
            console.log(response);
          });
      });
    },
    // Обновление товара
    UPDATE_PRODUCT(state, product: Product) {
      return new Promise((resolve, reject) => {
        axios
          .put('http://localhost:8090/product', product)
          .then((response) => {
            console.log(response);
          });
      });
    },
    // Удаление товара
    DELETE_PRODUCT(state, product_id: number) {
      return new Promise((resolve, reject) => {
        axios
          .delete('http://localhost:8090/product', {
            params: product_id,
          })
          .then((response) => {
            console.log(response);
          });
      });
    },
  },
  modules: {
  }
})
