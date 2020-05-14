import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false
Vue.prototype.$apiUrl = "http://localhost:5051";

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')