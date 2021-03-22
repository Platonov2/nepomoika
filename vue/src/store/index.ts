import Product from '@/models/Product'
import Vuex from 'vuex'
import axios from 'axios'
import Category from '@/models/Category'

export default new Vuex.Store({
  state: {
    adminToken: "" as string,
    userToken: "" as string,
    rootOfNewCategoryId: 0 as number,
    rootOfNewProductId: 0 as number,
    category: {} as Category,
    subcategories: [] as Category[],
    products: [] as Product[],
    editedCategory: {} as Category,
    editedProduct: {} as Product,
  },
  getters: {
    ADMIN_TOKEN: (state) => state.adminToken,
    USER_TOKEN: (state) => state.userToken,
    ROOT_OF_NEW_CATEGORY_ID: (state) => state.rootOfNewCategoryId,
    ROOT_OF_NEW_PRODUCT_ID: (state) => state.rootOfNewProductId,
    CATEGORY: (state) => state.category,
    SUBCATEGORIES: (state) => state.subcategories,
    PRODUCTS: (state) => state.products,
    EDITED_CATEGORY: (state) => state.editedCategory,
    EDITED_PRODUCT: (state) => state.editedProduct,
  },
  mutations: {
    SET_ADMIN_TOKEN: (state, adminToken) => {
      state.adminToken = adminToken;
    },
    SET_USER_TOKEN: (state, userToken) => {
      state.userToken = userToken;
    },
    SET_ROOT_OF_NEW_CATEGORY_ID: (state, rootOfNewCategoryId) => {
      state.rootOfNewCategoryId = rootOfNewCategoryId;
    },
    SET_ROOT_OF_NEW_PRODUCT_ID: (state, rootOfNewProductId) => {
      state.rootOfNewProductId = rootOfNewProductId;
    },
    SET_CATEGORY: (state, category) => {
      state.category = category;
    },
    SET_SUBCATEGORIES: (state, subcategories) => {
      state.subcategories = subcategories;
      console.log(state.subcategories);
    },
    SET_PRODUCTS: (state, products) => {
      state.products = products;
    },
    SET_EDITED_CATEGORY: (state, category) => {
      state.editedCategory = category;
    },
    SET_EDITED_PRODUCT: (state, product) => {
      state.editedProduct = product;
    },
    ADD_CATEGORY: (state, category) => {
      category[0].category_id = -1;
      state.subcategories.push(category[0]);
    },
    ADD_PRODUCT: (state, product) => {
      product[0].product_id = -1;
      state.products.push(product[0]);
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
    /**      АВТОРИЗАЦИЯ         */

    REGISTER(state, [username, password]) {
      const temp = {
        username: username,
        password: password,
        role: 'user'
      }
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8099/register', temp)
          .then((response) => {
            resolve(response);
            // this.dispatch('LOGIN', [ username, password ]);
          })
          .catch((error) => reject(error));
      });
    },

    LOGIN_ADMINISTRATOR(state, [username, password]) {
      const temp = {
        username: username,
        password: password
      }
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8099/login', temp)
          .then((response) => {
            resolve(response);
            this.commit('SET_ADMIN_TOKEN', response.data);
          })
          .catch((error) => reject(error));
      });
    },

    /**       КАТЕГОРИИ          */

    // Получение списка всех категорий
    ADMIN_GET_ROOT_CATEGORIES: (context) => {
      axios
        .get('http://localhost:8090/admin/category/roots')
        .then((response) => {
          context.commit('SET_CATEGORY', null);
          context.commit('SET_PRODUCTS', []);
          context.commit('SET_SUBCATEGORIES', response.data);
        });
    },
    MARKET_GET_ROOT_CATEGORIES: (context) => {
      axios
        .get('http://localhost:8090/catalog/category/roots')
        .then((response) => {
          context.commit('SET_CATEGORY', null);
          context.commit('SET_PRODUCTS', []);
          context.commit('SET_SUBCATEGORIES', response.data[0]);
        });
    },
    ADMIN_SET_CURRENT_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/admin/category', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_CATEGORY', response.data)
        });
    },
    MARKET_SET_CURRENT_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/catalog/category', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_CATEGORY', response.data)
        });
    },
    ADMIN_CHOOSE_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/admin/category/children', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_SUBCATEGORIES', response.data);
          context.dispatch('ADMIN_GET_PRODUCTS_BY_CATEGORY', category_id);
          context.dispatch('ADMIN_SET_CURRENT_CATEGORY', category_id);
          context.commit('SET_ROOT_OF_NEW_CATEGORY_ID', 0);
          context.commit('SET_ROOT_OF_NEW_PRODUCT_ID', 0);
        });
    },
    MARKET_CHOOSE_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/catalog/category/children', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_SUBCATEGORIES', response.data);
          context.dispatch('MARKET_GET_PRODUCTS_BY_CATEGORY', category_id);
          context.dispatch('MARKET_SET_CURRENT_CATEGORY', category_id);
        });
    },
    // Добавление новой категории
    POST_NEW_CATEGORY(state, category: Category) {
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8090/admin/category', category)
          .then((response) => {
            this.commit('ADD_CATEGORY', category);
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },
    // Обновление категории
    UPDATE_CATEGORY(state, category: Category) {
      return new Promise((resolve, reject) => {
        axios
          .put('http://localhost:8090/admin/category', category)
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
          .delete('http://localhost:8090/admin/category', {
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
    ADMIN_GET_PRODUCTS_BY_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/admin/products', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_PRODUCTS', response.data)
        });
    },
    MARKET_GET_PRODUCTS_BY_CATEGORY: (context, category_id: number) => {
      axios
        .get('http://localhost:8090/catalog/products', {
          params: {"category_id": category_id},
        })
        .then((response) => {
          context.commit('SET_PRODUCTS', response.data)
        });
    },
    // Добавление нового товара
    POST_NEW_PRODUCT(state, product: Product) {
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8090/admin/product', product)
          .then((response) => {
            this.commit('ADD_PRODUCT', product);
            resolve(response);
          })
          .catch((error) => reject(error));
      });
    },
    // Обновление товара
    UPDATE_PRODUCT(state, product: Product) {
      return new Promise((resolve, reject) => {
        axios
          .put('http://localhost:8090/admin/product', product)
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
          .delete('http://localhost:8090/admin/product', {
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
