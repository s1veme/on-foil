import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios";
import store from './vuex/store'


axios.defaults.baseURL = 'http://127.0.0.1:8000';

if (store.state.user.token) {
	console.log(store.state.user.token)
  axios.defaults.headers["Authorization"] =
    "Bearer " + store.state.user.token;
}

const app = createApp(App)
app.use(store)
app.mount('#app')