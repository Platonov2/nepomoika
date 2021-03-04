import Product from '@/models/Product'
import Vuex from 'vuex'
import axios from 'axios'
import Category from '@/models/Category'

export default new Vuex.Store({
  state: {
    category: {} as Category,
    subcategories: [] as Category[],
    products: [] as Product[],
  },
  getters: {
    CATEGORY: (state) => state.category,
    SUBCATEGORIES: (state) => state.subcategories,
    PRODUCTS: (state) => state.products,
  },
  mutations: {
    SET_CATEGORY: (state, category) => {
      state.category = category;
    },
    SET_SUBCATEGORIES: (state, subcategories) => {
      state.subcategories = subcategories;
    },
    SET_CURRENT_PRODUCTS: (state, products) => {
      state.products = products;
    },
  },
  actions: {
    /**       КАТЕГОРИИ          */

    // Получение списка всех категорий
    GET_ROOT_CATEGORIES: (context) => {
      axios
        .get('http://localhost:8090/category/roots')
        .then((response) => {
          context.commit('SET_CATEGORY', null)
          context.commit('SET_SUBCATEGORIES', response.data)
        });
    },
    CHANGE_CATEGORY: (context, category: Category) => {
      axios
        .get('http://localhost:8090/category/children', {
          params: category.category_id,
        })
        .then((response) => {
          context.commit('SET_CATEGORY', category);
          context.commit('SET_SUBCATEGORIES', response.data);
          context.dispatch('GET_PRODUCTS_BY_CATEGORY', category.category_id);
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
