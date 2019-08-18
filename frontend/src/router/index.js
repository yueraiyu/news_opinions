import Vue from 'vue'
import Router from 'vue-router'
import News from '@/components/News'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'News',
      component: News
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.length === 0) {  // 要前往的路由不存在时
    Vue.toasted.error('404: Not Found', { icon: 'fingerprint' })
    if (from.name) {
      next({
        name: from.name
      })
    } else {
      next({
        path: '/'
      })
    }
  } else {
    next()
  }
})

export default router
