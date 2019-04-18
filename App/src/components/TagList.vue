<template>
<div>
  <div class="container">
    <p>Список тегов</p>
  </div>
</div>
</template>

<script>
//import { watchList } from '../api'
import axios from 'axios'

export default {
  data () {
    return {
      articles: null,
      endpoint: 'https://jsonplaceholder.typicode.com/posts/',
    }
  },

  created() {
    this.getArticles();
  },

  methods: {
    /*
    getAllPostsExamp() {
      axios.get(this.endpoint)
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => {
          console.log('-----error-------');
          console.log(error);
        })
    },*/
    getArticles() {
      this.articles = require('../assets/example_news.json').articles;
    }
  }
}
</script>

<style>
.container {
  margin-top: 80px;
}
</style>
