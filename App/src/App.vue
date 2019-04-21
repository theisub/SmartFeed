<template>
  <div id="app">
    <Main v-bind:nickname="this.nickname"/>
  </div>
</template>

<script>
import Main from './components/Main.vue'

export default {
  name: 'app',
  
  components: {
    Main
  },

  data () {
    return {
      nickname: null,
    }
  },

  created() {
    this.askNickname();
  },

  methods: {
    askNickname() {
      this.nickname = prompt("Введите имя пользователя")
    },
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
