<template>
  <div>
    <!-- Navigation -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
          <a class="navbar-brand" href="#"> 问就是全栈 - 新闻分析 </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item active">
                <router-link v-bind:to="{ name: 'News'}" class="nav-link"> 论点
<!--                  <span class="sr-only">(current)</span>-->
                </router-link>
              </li>
              <li class="nav-item">
                <router-link v-bind:to="{ name: 'NewsAnalyzeTxt'}" class="nav-link">分析
                  <span class="sr-only">(current)</span>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div class="container">
        <!--  输入文本  -->
        <form @submit.prevent="onSubmit">
          <div class="form-group text-left">
            <label for="analyze_content" class="text-left">解析内容 : </label>
            <textarea class="form-control is-valid" id="analyze_content" v-model="content"  v-bind:readonly="isReadOnly" rows="15" placeholder="please enter ..." required></textarea>
          </div>
          <button type="submit" class="btn btn-primary" v-bind:hidden="isReadOnly">解析</button>
        </form>

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
      </div>
  </div>
</template>

<script>
    export default {
        name: "NewsAnalyzeTxt",
        data() {
            return {
              isReadOnly: false,
              content: undefined,
              opinions: undefined
            }
          },
        methods: {
          onSubmit(e){
            let path = `/api/news/analyze`
            let data = {content: this.content}
              this.$axios.post(path, data)
                .then((response) => {
                  // handle success
                  this.content = response.data.content
                  this.opinions = response.data.opinions

                  this.isReadOnly = true
                })
                .catch((error) => {
                  // handle error
                  console.log(error.response)
                })
          }
        }
    }
</script>

<style scoped>

</style>
