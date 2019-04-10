import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

// route-level code splitting
const ItemList = () => import('../views/ItemList.vue');
const TagList = () => import('../views/TagList.vue');

export function createRouter() {
    return new Router({
        mode: 'history',
        fallback: false,
        scrollBehavior: () => ({ y: 0 }),
        routes: [
            { path: '/news/:page(\\d+)?', component: ItemList },
            { path: '/tags/:id(\\d+)', component: TagList },
            { path: '/', redirect: '/news' }
        ]
    })
}