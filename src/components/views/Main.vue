<template>
  <div id="app">
    <header class="header">
      <nav class="inner">
        <div class="row">
          <div class="col-1">
            <router-link to="/" exact>
              <img class="logo" src="../../../public/logo.png" alt="logo">
            </router-link>
          </div>
          <div class="col-10">
            <div class="row pages">
              <div class="col">
                <router-link to="/news">Новости</router-link>
              </div>
              <div class="col">
                <router-link to="/tags">Интересы</router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </header>
    <transition name="fade" mode="out-in">
      <router-view class="view"></router-view>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'Main',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
  font-size: 15px;
  background-color: lighten(#eceef1, 30%);
  margin: 0;
  padding-top: 55px;
  color: #34495e;
  overflow-y: scroll;
}
.header {
  background-color: #5f76b6;
  position: fixed;
  z-index: 999;
  height: 70px;
  top: 0;
  left: 0;
  right: 0;
}
.logo {
  width: 80px;
  margin-right: 10px;
  display: inline-block;
  vertical-align: middle;
}
.pages {
  padding-top: 20px;
}
router-link {
  color: black;
  font-size: 25px;
  cursor: pointer;
}
</style>
