<template>
<div class="container">

  <div class="tags-data">
    <template class="col-md-4 news-block" v-for="tag in tags">
      <span class="badge badge-info" v-for="(value, key) in tag" :key="value.index">{{ key }}: {{ value }}</span>
    </template>
  </div>

  <div class="row justify-content-md-center tag-input-data">
    <div class="input-group col-md-6">

      <div class="input-group-prepend">
        <span class="input-group-text" id="basic-addon1">#</span>
        <span class="input-group-text" id="basic-addon1">Вес</span>
      </div>
      <input type="text" class="form-control col-md-4" placeholder="Тег" aria-label="Tag" aria-describedby="basic-addon1">
      <input type="text" class="form-control col-md-2" placeholder="0.5" aria-label="weight" aria-describedby="basic-addon1">
      <div class="input-group-append">
        <button v-on:click="addTag" class="btn btn-outline-info" type="button" id="button-add-tag">Добавить</button>
      </div>

    </div>
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
    },
    addTag() {
      // Высылаем тег на сервер
      getTags();
    },
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

.tag-input-data {
  padding-top: 50px;
}
</style>
