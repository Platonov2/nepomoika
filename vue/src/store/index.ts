import Product from '@/models/Product'
import Vuex from 'vuex'
import axios from 'axios'
import Category from '@/models/Category'

export default new Vuex.Store({
  state: {
    сategories: [] as Category[],
    currentCategory: {} as Category,
    currentProducts: [] as Product[],
    currentProduct: {} as Product,
  },
  getters: {
    CATEGORIES: (state) => state.сategories,
    CURRENT_PRODUCTS: (state) => state.currentProducts,
    CURRENT_PRODUCT: (state) => state.currentProduct,
  },
  mutations: {
    SET_CATEGORIES: (state, categories) => {
      state.сategories = categories;
    },
    SET_CURRENT_CATEGORY: (state, category) => {
      state.currentCategory = category;
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
        .get('http://localhost:8090/category')
        .then((response) => {
          context.commit('SET_CATEGORIES', response.data)
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
