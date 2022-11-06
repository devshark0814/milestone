import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/pages/Dashboard'
import Users from '@/pages/Users'
import Projects from '@/pages/Projects'
import Milestone from '@/pages/Milestone'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
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
      path: '/projects',
      name: 'Projects',
      component: Projects
    },
    {
      path: '/milestone',
      name: 'Milestone',
      component: Milestone
    }
  ]
})
