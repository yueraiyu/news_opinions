<template>
  <div>
    <!-- Page Content -->
    <div class="container">

      <div class="row">

        <!-- News Entries Column -->
        <div class="col-md-8">

<!--          <h1 class="my-4"> 实时要闻-->
<!--            <small>  </small>-->
<!--          </h1>-->

          <!-- News Post -->
          <div v-if="pages" class="card mb-4 border-0">
            <div v-for="(news, index) in pages.items" v-bind:key="index" class="card mb-4">
              <img class="card-img-top" src="../assets/news.jpg" alt="Card image cap">
              <div class="card-body">
                <h2 class="card-title">{{ news.title }}</h2>
                <p class="card-text text-left">{{ news.content }}</p>
                <router-link v-bind:to="{ name: 'NewsAnalyze', params: { id: news.id }}" class="btn btn-primary" style="float: right;"> 分析 &rarr;</router-link>
              </div>
              <div class="card-footer text-left">
                <router-link v-bind:to="{ name: 'NewsContent', params: { id: news.id }}">{{ news.source + " > " + news.author + " : " + news.title }}</router-link>
              </div>
            </div>
          </div>
          <!-- News Post -->

          <!-- Pagination -->
          <nav v-if="pages" aria-label="Page Navigation" class="g-mb-60">
            <ul class="list-inline">
              <li class="list-inline-item">
                <router-link v-bind:to="{ name: 'News', query: { search_value: search_value, page: pages._meta.page - 1, per_page: pages._meta.per_page }}" v-bind:class="{'u-pagination-v1__item--disabled': pages._meta.page == 1}" class="u-pagination-v1__item u-pagination-v1-1 g-rounded-50 g-pa-12-21" aria-label="Previous">
                  <span aria-hidden="true">
                    <i class="fa fa-angle-left"></i>
                  </span>
                  <span class="sr-only">Previous</span>
                </router-link>
              </li>

              <li v-if="page != 'NaN'" v-for="(page, index) in iter_pages" v-bind:key="index" class="list-inline-item g-hidden-sm-down">
                <router-link v-bind:to="{ name: 'News', query: { search_value: search_value, page: page, per_page: pages._meta.per_page }}" v-bind:class="{'u-pagination-v1-1--active': $route.query.page == page || (!$route.query.page && page == 1)}" class="u-pagination-v1__item u-pagination-v1-1 g-rounded-50 g-pa-12-19">{{ page }}</router-link>
              </li>
              <li v-else class="list-inline-item g-hidden-sm-down">
                <span class="g-pa-12-19">...</span>
              </li>

              <li class="list-inline-item">
                <router-link v-bind:to="{ name: 'News', query: { search_value: search_value, page: pages._meta.page + 1, per_page: pages._meta.per_page }}" v-bind:class="{'u-pagination-v1__item--disabled': pages._meta.page == pages._meta.total_pages }" class="u-pagination-v1__item u-pagination-v1-1 g-rounded-50 g-pa-12-21" aria-label="Next">
                  <span aria-hidden="true">
                    <i class="fa fa-angle-right"></i>
                  </span>
                  <span class="sr-only">Next</span>
                </router-link>
              </li>
<!--              <li class="list-inline-item float-right">-->
<!--                <span class="u-pagination-v1__item-info g-pa-12-19">Page {{ pages._meta.page }} of {{ pages._meta.total_pages }}</span>-->
<!--              </li>-->
            </ul>
          </nav>

        </div>

        <!-- Sidebar Widgets Column -->
        <div class="col-md-4">

          <!-- Search Widget -->
          <div class="card my-4">
            <h5 class="card-header">Search</h5>
            <div class="card-body">
              <div class="input-group">
                  <input type="text" v-model="search_value" class="form-control" placeholder="Search for...">
                  <span class="input-group-btn">
                      <router-link v-bind:to="{ name: 'News', query: { search_value: search_value }}" class="btn btn-secondary">GO!</router-link>
                  </span>
              </div>
            </div>
          </div>

          <!-- Categories Widget -->
<!--          <div class="card my-4">-->
<!--            <h5 class="card-header">Categories</h5>-->
<!--            <div class="card-body">-->
<!--              <div class="row">-->
<!--                <div class="col-lg-6">-->
<!--                  <ul class="list-unstyled mb-0">-->
<!--                    <li>-->
<!--                      <a href="#">Web Design</a>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                      <a href="#">HTML</a>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                      <a href="#">Freebies</a>-->
<!--                    </li>-->
<!--                  </ul>-->
<!--                </div>-->
<!--                <div class="col-lg-6">-->
<!--                  <ul class="list-unstyled mb-0">-->
<!--                    <li>-->
<!--                      <a href="#">JavaScript</a>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                      <a href="#">CSS</a>-->
<!--                    </li>-->
<!--                    <li>-->
<!--                      <a href="#">Tutorials</a>-->
<!--                    </li>-->
<!--                  </ul>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->

          <!-- Side Widget -->
<!--          <div class="card my-4">-->
<!--            <h5 class="card-header"> Side Widget </h5>-->
<!--            <div class="card-body">-->
<!--              You can put anything you want inside of these side widgets. They are easy to use, and feature the new Bootstrap 4 card containers!-->
<!--            </div>-->
<!--          </div>-->

        </div>

      </div>
      <!-- /.row -->
    </div>
    <!-- /.container -->
  </div>
</template>

<script>

  export default {
      name: "News",
      data() {
        return {
          pages: '',
          search_value: ''
        }
      },
      methods: {
        search () {
          let page = 1
          let per_page = 10

          if (typeof this.$route.query.page != 'undefined') {
            page = this.$route.query.page
          }
          if (typeof this.$route.query.per_page != 'undefined') {
            per_page = this.$route.query.per_page
          }

          let path = `/api/news?page=${page}&per_page=${per_page}`

          let search_value = undefined
          if (typeof this.$route.query.search_value != 'undefined'){
            search_value = this.$route.query.search_value
            path += `&search_value=${search_value}`
          }

          this.$axios.get(path)
            .then((response) => {
              // handle success
              this.pages = response.data
              this.search_value = this.pages.search_value
              console.log(this.search_value)

              // 构建分页导航，当前页左、右两边各显示2页，比如  1, 2, ... 7, 8, 9, 10, 11 ... 30, 31
              let arr = [1, this.pages._meta.page-1, this.pages._meta.page, this.pages._meta.page+1, this.pages._meta.total_pages-1, this.pages._meta.total_pages]
              // 小于1，或大于最大页数的都是非法的，要去除
              arr = arr.filter(item => item > 0 && item <= this.pages._meta.total_pages)
              // 去除重复项
              this.iter_pages = [...new Set(arr)]
              // 假设当前页为1，总页数为6或6以上时，在倒数第2个位置插入特殊标记  1, 2, 3 ... 5, 6
              if (this.pages._meta.page + 2 < this.pages._meta.total_pages - 2) {
                this.iter_pages.splice(-2, 0, 'NaN')
              }
              // 当前页为6或6以上时，在第3个位置插入特殊标记  1, 2 ... 4, 5, 6
              if (this.pages._meta.page - 3 > 2) {
                this.iter_pages.splice(2, 0, 'NaN')
              }
            })
            .catch((error) => {
              // handle error
              console.log(error.response)
            })
        }
      },
      created () {
        this.search()
      },
      // 当查询参数 page 或 per_page 变化后重新加载数据
      beforeRouteUpdate (to, from, next) {
        next()
        this.search()
      }
  }
</script>

<style scoped>

</style>
