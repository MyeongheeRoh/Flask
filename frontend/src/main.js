import Vue from 'vue'
import router from './router'
import App from './App.vue'
import store from './store'
import { BootstrapVue , IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import BaseLayoutModifier from '@/components/BaseLayoutModifier'
import BaseBlock from '@/components/BaseBlock'
import BasePageHeading from '@/components/BasePageHeading'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.component(BaseLayoutModifier.name, BaseLayoutModifier)
Vue.component(BasePageHeading.name, BasePageHeading)
Vue.component(BaseBlock.name, BaseBlock)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
