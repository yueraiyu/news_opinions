import Vue from 'vue'
import Router from 'vue-router'
import NewsContent from '@/components/NewsContent'
import NewsAnalyze from '@/components/NewsAnalyze'
import NewsAnalyzeTxt from '@/components/NewsAnalyzeTxt'
import News from '@/components/News'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'News',
      component: News
    },
    {
      path: '/news/:id',
      name: 'NewsContent',
      component: NewsContent
    },
    {
      path: '/news/analyze/:id',
      name: 'NewsAnalyze',
      component: NewsAnalyze
    },
    {
      path: '/news/analyze/',
      name: 'NewsAnalyzeTxt',
      component: NewsAnalyzeTxt
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
