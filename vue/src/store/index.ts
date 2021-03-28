import Product from '@/models/Product'
import Vuex from 'vuex'
import axios from 'axios'
import Category from '@/models/Category'

export default new Vuex.Store({
  state: {
    token: "" as string,
    rootOfNewCategoryId: 0 as number,
    rootOfNewProductId: 0 as number,
    category: {} as Category,
    subcategories: [] as Category[],
    products: [] as Product[],
    editedCategory: {} as Category,
    editedProduct: {} as Product,
    cartProducts: [] as Product[],
    finalPrice: 0 as number,
  },
  getters: {
    TOKEN: (state) => {
      const results = document.cookie.match(/token=(.+?)(;|$)/);
      if (results != null) {
        return results[1];
      }
      else "";
    },
    ROOT_OF_NEW_CATEGORY_ID: (state) => state.rootOfNewCategoryId,
    ROOT_OF_NEW_PRODUCT_ID: (state) => state.rootOfNewProductId,
    CATEGORY: (state) => state.category,
    SUBCATEGORIES: (state) => state.subcategories,
    PRODUCTS: (state) => state.products,
    EDITED_CATEGORY: (state) => state.editedCategory,
    EDITED_PRODUCT: (state) => state.editedProduct,
    CART_PRODUCTS: (state) => state.cartProducts,
    FINAL_PRICE: (state) => state.finalPrice,
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      document.cookie = "token=" + token;
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
    },
    SET_PRODUCTS: (state, products) => {
      console.log(products);
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
    },
    SET_CART_PRODUCTS: (state, cartProducts) => {
      state.cartProducts = cartProducts;
    },
    SET_FINAL_PRICE: (state, finalPrice) => {
      state.cartProducts = finalPrice;
    },
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
            this.dispatch('LOGIN', [ username, password ]);
          })
          .catch((error) => reject(error));
      });
    },

    LOGIN(state, [username, password]) {
      const temp = {
        username: username,
        password: password
      }
      return new Promise((resolve, reject) => {
        axios
          .post('http://localhost:8099/login', temp)
          .then((response) => {
            resolve(response);
            this.commit('SET_TOKEN', response.data.access_token);
          })
          .catch((error) => reject(error));
      });
    },

    /**       КАТЕГОРИИ          */

    // Получение списка всех категорий
    ADMIN_GET_ROOT_CATEGORIES: (context) => {
      console.log(context.getters.TOKEN);
      const headers = {
        'Authorization': "Bearer " + context.getters.TOKEN,
      }
      axios
        .get('http://localhost:8099/admin/category/roots', {
          headers: headers
        })
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
          console.log(response.data)
          context.commit('SET_CATEGORY', null);
          context.commit('SET_PRODUCTS', []);
          context.commit('SET_SUBCATEGORIES', response.data);
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

    /**       КОРЗИНА          */

    GET_CART_PRODUCTS: (context) => {
      const headers = {
        'Authorization': "Bearer " + context.getters.TOKEN,
      }
      axios
        .get('http://localhost:8099/cart/get', {
          headers: headers
        })
        .then((response) => {
          // console.log(response.data);
          console.log(response.data.product_dict);
          console.log(response.data.sum);
          context.commit('SET_CART_PRODUCTS', response.data.product_dict);
          context.commit('SET_FINAL_PRICE', response.data.sum);
        });
    },
  },
  modules: {
  }
})
