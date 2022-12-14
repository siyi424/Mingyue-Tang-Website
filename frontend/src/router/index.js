import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/info',
    name: 'info',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/InfoView.vue')
  },
  {
    path: '/search/:name',
    name: 'search',
    component: () => import('../views/search/ListView.vue'),
    props: true,
    children: [{
      path: 'singleChat/:person',
      name: 'singleChat',
      component: () => import('../views/search/SingleRoom.vue'),
      props: true
    }]
  },
]

const router = createRouter({
  base: '/',
  // history: createWebHistory(process.env.BASE_URL),
  history: createWebHistory("/"),
  routes
})

export default router
