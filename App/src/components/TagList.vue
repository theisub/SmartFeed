<template>
<div class="container">

  <div class="tags-data">
    <template 
      class="col-md-4 news-block" 
      v-for="tag in tags"
    >
      <span 
        class="badge badge-info" 
        v-for="(value, key) in tag" 
        :key="value.index"
      >
        {{ key }}: {{ value }}
      </span>
    </template>
  </div>

  <div class="row justify-content-md-center tag-input-data">
    <div class="input-group col-md-9">

      <div class="input-group-prepend">
        <span class="input-group-text">#</span>
        <span class="input-group-text">Вес</span>
      </div>
      <input 
        type="text" 
        class="form-control col-md-6" 
        placeholder="Тег" 
      >
      <input 
        type="number" 
        step="0.1" 
        min="0"
        max="1"
        class="form-control col-md-3" 
        v-bind:placeholder="newTagValue" 
        v-bind:value="newTagValue"
      >
      <div class="input-group-append">
        <button 
          class="btn btn-outline-info" 
          type="button" 
          v-on:click="addTag()" 
        >Добавить</button>
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
      newTagName: "",
      newTagValue: 0.5,
      //endpoint: 'https://jsonplaceholder.typicode.com/posts/',
    }
  },

  created() {
    this.getTags();
  },

  methods: {
    getTags() {
      this.tags = require('../assets/example_tags.json').tags;
      /*
      const strJson = JSON.stringify({
        "nickname": this.nickname,
      });
      // тут поправить аккуратно ссылку на запрос
      axios.post(this.endpoint + '', strJson)
        .then(response => {
          this.articles = this.articles.concat(response.data.articles);
        })
        .catch(error => {
          console.log('-----error-------', error);
        })
      */
    },
    addTag(key, value) {
      /*
      const strJson = JSON.stringify({
        "nickname": this.nickname,,
        "tags": [
            {key: value}
        ]
      });
      // тут поправить аккуратно ссылку на запрос
      axios.post(this.endpoint + '', strJson)
        .catch(error => {
          console.log('-----error-------', error);
        })
      */
      this.getTags()
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
