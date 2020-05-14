import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import '@mdi/font/css/materialdesignicons.css'
import 'buefy/dist/buefy.css'

Vue.config.productionTip = false
Vue.use(Buefy)
Vue.prototype.$apiUrl = "http://localhost:3000";

new Vue({
  render: h => h(App)
}).$mount('#app')
