import Vue from 'vue'
import Router from 'vue-router'
import ItemList from '../components/ItemList.vue'
import TagList from '../components/TagList.vue'

Vue.use(Router);

// route-level code splitting
//const ItemList = () => import('../components/ItemList.vue');
//const TagList = () => import('../components/TagList.vue');

export function createRouter() {
    return new Router({
        mode: 'history',
        fallback: false,
        scrollBehavior: () => ({ y: 0 }),
        routes: [
            { path: '/news/', component: ItemList },
            { path: '/tags/', component: TagList },
            { path: '/', redirect: '/news' }
        ]
    })
}