import Vue from 'vue';
import Router from 'vue-router';

import Default from '../components/Default.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Default',
      component: Default,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
