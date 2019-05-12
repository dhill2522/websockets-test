<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <button @click="connect()">Connect</button>
    <button @click="send()">Send</button>
    <p v-for="(msg, id) in messages" v-bind:key="id">{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {},
  data: function() { return {
    title: 'Testing websockets with Vue and Python',
    serverAddress: 'ws://localhost:5000',
    ws: null,
    messages: [],
    counter: 0
  }},
  methods: {
    connect: function() {
      console.log('Connecting...')
      this.ws = new WebSocket(this.serverAddress)
      this.ws.addEventListener('open', this.onOpen)
      this.ws.addEventListener('message', this.onMessage)

    },
    onOpen: function(event) {
      console.log('Connection opened:', event)
      this.messages.push('WebSocket connected')
    },
    onMessage: function(event) {
      console.log('Message received:', event)
      this.messages.push(event.data)
    },
    send: function() {
      if (this.ws) {
        this.counter ++
        this.ws.send('Message '+this.counter)
      } else {
        this.messages.push('Error: Websocket not connected yet.')
      }
    },
    clearMessages: function() {
      this.messages = []
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
