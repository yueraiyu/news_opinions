<template>
    <div class="container">
      <!--  解析详情  -->
      <table v-if="opinions" class="table table-hover table-bordered">
        <thead>
          <tr>
            <th scope="col">姓名</th>
            <th scope="col">动作</th>
            <th scope="col">观点</th>
          </tr>
        </thead>
        <tbody v-for="(opinion, index) in opinions" v-bind:key="index">
          <tr>
            <td>{{opinion.name}}</td>
            <td>{{opinion.action}}</td>
            <td>{{opinion.words}}</td>
          </tr>
        </tbody>
      </table>

      <!--  文本详情    -->
<!--      <div v-for="(txt, index) in news.content.split('\\n')" v-bind:key="index">-->
<!--        <h1 class="lead font-weight" v-if="index == 0">{{txt}}</h1>-->
<!--        <h1 class="lead font-weight text-xl-left" v-if="index == 1">{{txt}}</h1>-->
<!--        <p class="text-xl-left" v-if="index > 1">{{txt}}</p>-->
<!--      </div>-->
    </div>
</template>

<script>
    export default {
        name: "NewsAnalyze",
        data() {
            return {
              news: "",
              opinions: []
            }
          },
        methods: {
          analyze(){
            let news_id = undefined

            if (typeof this.$route.params.id != 'undefined') {
              news_id = this.$route.params.id
              let path = `/api/news/analyze/${news_id}`
              this.$axios.get(path)
                .then((response) => {
                  // handle success
                  this.news = response.data.news
                  this.opinions = response.data.opinions
                })
                .catch((error) => {
                  // handle error
                  console.log(error.response)
                })
            }
          }
        },
        created () {
          this.analyze()
        }
    }
</script>

<style scoped>

</style>
