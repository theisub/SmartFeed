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
        ref="new_tag_name"
        type="text" 
        class="form-control col-md-6" 
        placeholder="Тег" 
      >
      <input 
        ref="new_tag_value"
        type="number" 
        step="0.01" 
        min="0"
        max="1"
        class="form-control col-md-3" 
        v-bind:placeholder="0.5" 
        v-bind:value="0.5" 
      >
      <div class="input-group-append">
        <button 
          class="btn btn-outline-info" 
          type="button" 
          v-on:click="addTag()" 
        >
          Добавить
        </button>
      </div>

    </div>
  </div>

</div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    nickname: String,
    endpoint: String,
  },

  data () {
    return {
      tags: null,
    }
  },

  created() {
    this.startTimer();
  },

  methods: {
    getTags() {
      
      const strJson = JSON.stringify({
        "nickname": this.nickname,
      });
      axios.post(this.endpoint + 'get_user_tags/', strJson)
        .then(response => {
          this.tags = response.data.tags;
        })
        .catch(error => {
          console.log('-----error-------', error);
        })
      
    },
    addTag() {
      
      const key = this.$refs.new_tag_name.value;
      console.log(key)
      const value = this.$refs.new_tag_value.value;
      console.log(value)

      const strJson = JSON.stringify({
        "nickname": this.nickname,
        "tags": [
          {
            [key]: value
          }
        ]
      });
      console.log(strJson)
      axios.post(this.endpoint + 'init_user/', strJson)
        .catch(error => {
          console.log('-----error-------', error);
        })

    },
	    stopTimer () {
	      	if (this.interval) {
	        	window.clearInterval(this.interval)
	      	}
	    },
	    startTimer () {
	      	this.stopTimer()
	      	this.interval = window.setInterval(() => {
	        	this.getTags()
	      	}, 1000)
	    },
  }
}
</script>

<style scoped>
* {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
}

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
