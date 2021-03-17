import Product from '@/models/Product'
import Vuex from 'vuex'
import axios from 'axios'
import Category from '@/models/Category'

export default new Vuex.Store({
  state: {
    category: {} as Category,
    subcategories: [] as Category[],
    products: [] as Product[],
    editedCategory: {} as Category,
    editedProduct: {} as Product,
  },
  getters: {
    CATEGORY: (state) => state.category,
    SUBCATEGORIES: (state) => state.subcategories,
    PRODUCTS: (state) => state.products,
    EDITED_CATEGORY: (state) => state.editedCategory,
    EDITED_PRODUCT: (state) => state.editedProduct,
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
      console.log(state.products)
    },
    SET_EDITED_CATEGORY: (state, category) => {
      state.editedCategory = category;
    },
    SET_EDITED_PRODUCT: (state, product) => {
      state.editedProduct = product;
    },
    DELETE_CATEGORY: (state, category_id) => {
      for (let i = 0; i < state.subcategories.length; i++) {
        const category = state.subcategories[i];
        if (category.category_id == category_id) {
          state.subcategories.splice(i, 1);
          break;
        }
      }
    },
    DELETE_PRODUCT: (state, product_id) => {
      for (let i = 0; i < state.products.length; i++) {
        const product = state.products[i];
        if (product.product_id == product_id) {
          state.products.splice(i, 1);
          break;
        }
      }
    }
  },
  actions: {
    /**       КАТЕГОРИИ          */

    // Получение списка всех категорий
    GET_ROOT_CATEGORIES: (context) => {
      axios
        .get('http://localhost:8090/category/roots')
        .then((response) => {
          context.commit('SET_CATEGORY', null)
          context.commit('SET_CURRENT_PRODUCTS', null)
          context.commit('SET_SUBCATEGORIES', response.data)
        });
    },
    SET_CURRENT_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/category', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_CATEGORY', response.data)
        });
    },
    CHOOSE_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/category/children', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_SUBCATEGORIES', response.data);
          context.dispatch('GET_PRODUCTS_BY_CATEGORY', category_id);
        });
    },
    // Добавление новой категории
    POST_NEW_CATEGORY(state, category: Category) {
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8090/category', category)
          .then((response) => {
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },
    // Обновление категории
    UPDATE_CATEGORY(state, category: Category) {
      return new Promise((resolve, reject) => {
        axios
          .put('http://localhost:8090/category', category)
          .then((response) => {
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },
    // Удаление категории
    DELETE_CATEGORY(state, category_id: number) {
      this.commit('DELETE_CATEGORY', category_id);

      return new Promise((resolve, reject) => {
        axios
          .delete('http://localhost:8090/category', {
            params: {"category_id": category_id},
          })
          .then((response) => {
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },

    /**       ТОВАРЫ          */

    // Получение всех товаров из категории по его id
    GET_PRODUCTS_BY_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/products', {
          params: {"category_id": category_id},
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
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },
    // Обновление товара
    UPDATE_PRODUCT(state, product: Product) {
      return new Promise((resolve, reject) => {
        axios
          .put('http://localhost:8090/product', product)
          .then((response) => {
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },
    // Удаление товара
    DELETE_PRODUCT(state, product_id: number) {
      this.commit('DELETE_PRODUCT', product_id);

      return new Promise((resolve, reject) => {
        axios
          .delete('http://localhost:8090/product', {
            params: {"product_id": product_id},
          })
          .then((response) => {
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },
  },
  modules: {
  }
})
