import Product from '@/models/Product'
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    products: [] as Product[],
  },
  getters: {
    PRODUCTS: (state) => state.products,
  },
  mutations: {
    SET_PRODUCTS: (state, products) => {
      state.products = products;
    }
  },
  actions: {
    GET_PRODUCTS: (context) => {
      axios.get('http://localhost:8090/api/products/')
        .then((response) => {
          context.commit('SET_PRODUCTS', response.data)
        });
    }
  },
  modules: {
  }
})
