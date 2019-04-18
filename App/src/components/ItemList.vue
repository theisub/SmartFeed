<template>
<div>
  <div class="container">
    <div class="row">
      <div class="col-md-4 news-block" v-for="article in articles" :key="article.index">
        <a v-bind:href="article.url" target="_blank">
          <div>
            <img v-bind:src="article.img" class="img-fluid">
            <h1>{{ article.title }}</h1>
            <h2>{{ article.description }}</h2>
          </div>
        </a>
      </div>
    </div>

    <button type="button" class="btn btn-dark">Еще 9 новостей</button>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      articles: [],
      //endpoint: 'https://jsonplaceholder.typicode.com/posts/',
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
      //this.articles = this.articles.concat(require('../assets/example_news.json').articles);
    },
  }
}
</script>

<style>
* {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
}

a:-webkit-any-link {
  text-decoration-color: grey;
}

img {
  padding: 10px;
}

h1,h2 {
  padding-right: 10px;
  padding-left: 10px;
  color: grey;;
}

h1 {
  font-size: 18px;
}

h2 {
  font-size: 10px;
}

button {
  margin: 20px;
  margin-bottom: 100px;
}

.container {
  margin-top: 80px;
}

.news-block  {
  padding: 10px;
  cursor: pointer;
  background: #CEE3F6;
  background-clip: content-box;
}
</style>