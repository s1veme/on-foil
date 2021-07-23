<template>
  <div id="app">
    <h2>Vue.js WebSocket Tutorial</h2> 
    <v-login />
  </div>
</template>

<script>
import vLogin from '@/components/v-login.vue'
export default {
  name: 'App',
  data: function() {
    return {
      connection: null,
    }
  },
  created: function() {
    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket(
      "ws://127.0.0.1:8000/connect"
      + "?token="
      + this.$store.state.user.token
    )

    this.connection.onmessage = function(event) {
      console.log(event);
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }
  },

  components: {
    vLogin
  }
}
</script>

<style>
</style>
