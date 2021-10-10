<template>
  <a-menu mode="horizontal">
    <a-menu-item key="1">
      <router-link to="/esdls">ESDL List</router-link>
    </a-menu-item>
    <a-menu-item key="2">
      <router-link to="/add">Add Esdl</router-link>
    </a-menu-item>
  </a-menu>
  <router-view />
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style></style>
