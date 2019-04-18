<template>
<div>
  <div v-for="news in newsList" :key="news">
    {{ news.title }}
  </div>
  <div v-for="post in posts" :key="post">
    {{ post.title }}
  </div>
</div>
</template>

<script>
//import { watchList } from '../api'
import axios from 'axios'

export default {
  data () {
    return {
      posts: null,
      endpoint: 'https://jsonplaceholder.typicode.com/posts/',
      newsList: null,
    }
  },

  created() {
    this.getAllPostsExamp();
    this.getAllPostsBlanc();
  },

  methods: {
    getAllPostsExamp() {
      axios.get(this.endpoint)
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => {
          console.log('-----error-------');
          console.log(error);
        })
    },
    getAllPostsBlanc() {
      axios.get(this.endpoint)
        .then(response => {
          this.newsList = response.data;
        })
        .catch(error => {
          console.log('-----error-------');
          console.log(error);
        })
    }
  }
}
</script>

<style>
</style>