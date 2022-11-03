import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Dashboard from '@/pages/Dashboard'
import Users from '@/pages/Users'
import Milestone from '@/pages/Milestone'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/users',
      name: 'Users',
      component: Users
    },
    {
      path: '/milestone',
      name: 'Milestone',
      component: Milestone
    }
  ]
})
