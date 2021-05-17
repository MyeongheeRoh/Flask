import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping'

// Main layouts
import LayoutBackend from '@/layouts/variations/Backend.vue'
import LayoutSimple from '@/layouts/variations/Simple.vue'

Vue.use(Router);

// Frontend: Landing
const Landing = () => import("@/views/Landing.vue")

// Backend: General
const Dashboard = () => import(/* webpackChunkName: "pages-dashboard", webpackPrefetch: true */"@/views/Dashboard.vue")

const ElementsRibbons = () => import("@/views/elements/Ribbons.vue")

// Router Configuration
export default new Router({
  linkActiveClass: 'active',
  linkExactActiveClass: '',
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/backend',
      redirect: '/backend/dashboard',
      component: LayoutBackend,
      children: [
        {
          path: 'dashboard',
          name: 'dashboard',
          component: Dashboard,
        },
        {
          path: 'elements',
          redirect: '/elements/grid',
          component: {
            render(c) { return c('router-view') }
          },
          children: [
            {
              path: 'ribbons',
              name: 'Elements Ribbons',
              component: ElementsRibbons
            },
          ]
        },
      ]
    },
  ]
});