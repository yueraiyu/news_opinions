<template>
  <div>
    <!-- Page Content -->
    <div class="container">
      <div class="row">

        <!-- Post Content Column -->
        <div v-if="news" class="col-lg-10">

          <!-- Title -->
          <h1 class="mt-4">{{news.title}}</h1>

          <!-- Author -->
          <p class="lead">
            <a href="#">{{news.source + " > " + news.author}}</a>
          </p>

          <hr>

          <!-- Preview Image -->
          <img class="img-fluid rounded" src="../assets/news.jpg" alt="">

          <hr>

          <!-- Post Content -->
          <div v-for="(txt, index) in news.content.split('\\n')" v-bind:key="index">
            <h1 class="lead font-weight" v-if="index == 0">{{txt}}</h1>
            <h1 class="lead font-weight text-xl-left" v-if="index == 1">{{txt}}</h1>
            <p class="text-xl-left" v-if="index > 1">{{txt}}</p>
          </div>
          <hr>
        </div>
      </div>
      <!-- /.row -->

    </div>
    <!-- /.container -->
  </div>
</template>

<script>
    export default {
        name: "NewsContent",
        data() {
          return {
            news: ""
          }
        },
        methods: {
          content(){
            let news_id = undefined

            if (typeof this.$route.params.id != 'undefined') {
              news_id = this.$route.params.id
              let path = `/api/news/${news_id}`
              this.$axios.get(path)
                .then((response) => {
                  // handle success
                  this.news = response.data
                })
                .catch((error) => {
                  // handle error
                  console.log(error.response)
                })
            }
          }
        },
        created () {
          this.content()
        }
    }
</script>

<style scoped>

</style>
