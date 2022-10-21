import { createRouter, createWebHashHistory } from "vue-router";

import HomePage from '../components/HomePage.vue'

const routes = [
    {path: '/', component: HomePage},
];

const router = createRouter({
    routes,
    history: createWebHashHistory()
});

export default router;