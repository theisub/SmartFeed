<template>
<div>
  <div v-for="article in articles" :key="article.index">
    <a v-bind:href="article.url" target="_blank">
      <div>
        <h5>{{ article.title }}</h5>
        <p>{{ article.description }}</p>
        <img v-bind:src="article.img">
      </div>
    </a>
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
</style>