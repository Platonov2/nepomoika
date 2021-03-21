<template>
  <div>
    <div id="main">
      <AdminHeader id="adminHeader"/>
      <AdminLists id="adminLists"/>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AdminHeader from './AdminHeader.vue';
import AdminLists from './AdminLists.vue';

@Component({
  components: {
    AdminHeader,
    AdminLists,
  },
})
export default class AdminMainPage extends Vue {

  mounted() {
    if (this.$store.getters.ADMIN_TOKEN == "") {
      this.$router.push('/admin/login');
    }
  }
}
</script>

<style lang="scss">

#main {
}

</style>