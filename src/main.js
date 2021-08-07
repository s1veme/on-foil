import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'

import 'reset-css'
import './assets/base.sass'

window.axios = require('axios');
axios.defaults.baseURL = 'http://127.0.0.1:8000';

if (localStorage.getItem('token')) {
  axios.defaults.headers["Authorization"] =
    "Bearer " + localStorage.getItem('token');
}

const app = createApp(App)
app.use(router)
app.mount('#app')

