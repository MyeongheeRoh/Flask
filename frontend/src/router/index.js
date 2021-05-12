import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping'

// Main layouts
import LayoutBackend from '@/layouts/variations/Backend.vue'
import LayoutBackendBoxed from '@/layouts/variations/BackendBoxed.vue'
import LayoutSimple from '@/layouts/variations/Simple.vue'

Vue.use(Router);

// Frontend: Landing
const Landing = () => import("@/views/Landing.vue")

// Backend: General
const Dashboard = () => import(/* webpackChunkName: "pages-dashboard", webpackPrefetch: true */"@/views/Dashboard.vue")

// Pages: Boxed Backend
const BoxedDashboard = () => import(/* webpackChunkName: "pages-boxed-dashboard" */"@/views/pages/boxed/Dashboard.vue")
const BoxedSearch = () => import("@/views/pages/boxed/Search.vue")
const BoxedSimple1 = () => import("@/views/pages/boxed/Simple1.vue")
const BoxedSimple2 = () => import("@/views/pages/boxed/Simple2.vue")
const BoxedImage1 = () => import("@/views/pages/boxed/Image1.vue")
const BoxedImage2 = () => import("@/views/pages/boxed/Image2.vue")

// Router Configuration
export default new Router({
  linkActiveClass: 'active',
  linkExactActiveClass: '',
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/',
      component: LayoutSimple,
      children: [
        {
          path: '/',
          name: 'Home',
          component: Landing
        },
      ]
    },
    {
      path: '/backend-boxed',
      redirect: '/backend-boxed/dashboard',
      component: LayoutBackendBoxed,
      children: [
        {
          path: 'dashboard',
          name: 'Boxed Dashboard',
          component: BoxedDashboard
        },
        {
          path: 'search',
          name: 'Boxed Search',
          component: BoxedSearch
        },
        {
          path: 'simple1',
          name: 'Boxed Simple1',
          component: BoxedSimple1
        },
        {
          path: 'simple2',
          name: 'Boxed Simple2',
          component: BoxedSimple2
        },
        {
          path: 'image1',
          name: 'Boxed Image1',
          component: BoxedImage1
        },
        {
          path: 'image2',
          name: 'Boxed Image2',
          component: BoxedImage2
        }
      ]
    },
  ]
});