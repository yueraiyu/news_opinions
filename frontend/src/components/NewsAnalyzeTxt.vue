<template>
    <div class="container">
      <!--  输入文本  -->
      <form>
        <div class="form-group">
          <label for="analyze_content">解析内容</label>
          <textarea class="form-control is-valid" id="analyze_content" rows="15" placeholder="please enter ..." required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">解析</button>
      </form>

      <!--  解析详情  -->
      <table v-if="opinions" class="table table-hover table-bordered hide">
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
</template>

<script>
    export default {
        name: "NewsAnalyzeTxt"
    }
</script>

<style scoped>

</style>
