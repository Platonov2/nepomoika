<template>
  <div id="app">
    <router-view id="body"/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Vuex from 'vuex';
import VueRouter, { RouteConfig } from 'vue-router';

Vue.use(Vuex)
Vue.use(VueRouter)

@Component
export default class App extends Vue {
}
</script>

<style lang="scss">
</style>
