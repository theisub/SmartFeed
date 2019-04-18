<template>
<div class="container">
  <div class="tags-data">
    <template class="col-md-4 news-block" v-for="tag in tags">
      <span class="badge badge-info" v-for="(value, key) in tag" :key="value.index">{{ key }}: {{ value }}</span>
    </template>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      tags: null,
      //endpoint: 'https://jsonplaceholder.typicode.com/posts/',
    }
  },

  created() {
    this.getTags();
    console.log(this.tags)
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
    getTags() {
      this.tags = require('../assets/example_tags.json').tags;
    }
  }
}
</script>

<style>
.badge {
  margin: 5px;
  font-size: 20px;
}

.container {
  margin-top: 80px;
}

.tags-data {
  margin-top: 180px;
}
</style>
