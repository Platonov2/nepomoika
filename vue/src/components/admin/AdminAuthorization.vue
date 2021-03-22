<template>
  <div>
    <div id="authorizationForm">
      <div id="title">
        Авторизация
      </div>
      <div id="inputs">
        <input class="input"
          v-model.lazy.trim="username"
          placeholder="Логин"
        />
        <input class="input"
          type="password"
          v-model.lazy.trim="password"
          placeholder="Пароль"
        />
        <div id="error">
          {{ error }}
        </div>
        <button id="loginButton" class="input" v-on:click="onAddCategoryClick">
          <div id="loginButton-text">Авторизоваться</div>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class AdminAuthorization extends Vue {
  username = "";
  password = "";
  error = "";

  onAddCategoryClick() {
    this.$store.dispatch('LOGIN', [this.username, this.password])
      .then(() => this.$router.push('/admin'))
      .catch(() => this.error = "Неверный логин или пароль");
  }
}
</script>

<style lang="scss">

#authorizationForm {
  display: block;
  box-shadow: 1.5px 1.5px 6px rgb(100, 100, 100);
  width: 400px;
  margin-top: 150px;
  margin-left: calc(50% - 250px);

  #title {
    display: block;
    text-align: center;
    font-size: 30pt;
    font-weight: bold;
    color: rgb(51, 51, 51);
    padding: 20px 0px;
  }

  #inputs {
    display: block;
    margin: 20px 40px;
    padding-bottom: 20px;

    .input {
      display: block;
      width: 100%;
      font-size: 18pt;
      margin-bottom: 15px;
    }

    #error {
      display: block;
      margin-top: 10px;
      height: 14pt;
      color: red;
    }

    #loginButton {
      display: block;
      margin-left: 3px;
      padding-bottom: 10px;
      margin-top: 30px;
      cursor: pointer;

      #loginButton-text {
        margin-top: 10px;
      }
    }
  }
}

</style>