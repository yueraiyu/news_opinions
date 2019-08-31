<template>
  <div>
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
                  this.content = response.data.news
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
