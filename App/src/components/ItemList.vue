<template>
<div class="container">

  <div class="row">

    <div 
      class="col-md-4 news-block" 
      v-for="article in articles" 
      :key="article.index">
      <a 
        target="_blank"
        v-on:click="incArticleTags(article)" 
        v-bind:href="article.url" 
      >
        <div>
          <img 
            class="img-fluid"
            v-bind:src="article.img" 
          >
          <h1>
            {{ article.title }}
          </h1>
          <h2>
            {{ article.description }}
          </h2>
        </div>
      </a>
    </div>

  </div>

  <button 
    type="button" 
    class="btn btn-dark get-articles"
    v-on:click="getArticles('more')" 
  >
    Еще новости
  </button>

</div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    nickname: String,
  },

  data () {
    return {
      articles: [],
      endpoint: 'http://127.0.0.1:8000/news/',
    }
  },

  created() {
    this.getArticles('refresh');
    console.log(this.nickname)
  },

  methods: {
    getArticles(param) {
      
      const strJson = JSON.stringify({
        "nickname": this.nickname,
        "param": param,
      });
      axios.post(this.endpoint + 'get_news/', strJson)
        .then(response => {
          this.articles = this.articles.concat(response.data.articles);
        })
        .catch(error => {
          console.log('-----error-------', error);
        })
      
    },
    incArticleTags: function (article) {
      
      const strJson = JSON.stringify({
        "nickname": this.nickname,
        "url": article.url,
      });
      axios.post(this.endpoint + 'news_click/', strJson)
        .catch(error => {
          console.log('-----error-------', error);
        })
      
    },
  }
}
</script>

<style scoped>
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

.get-articles {
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