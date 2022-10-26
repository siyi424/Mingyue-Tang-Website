<template>
  <div class="searchList">
    <el-row :gutter="20" v-for="value in items" :key="value.desc">
      <el-col :span="6">{{value.name}}</el-col>
      <el-col :span="6">{{value.birth}}</el-col>
      <el-col :span="6">{{value.passDate}}</el-col>
      <el-col :span="6">{{value.gender}}</el-col>
    </el-row>
  </div>
</template>

<script>
export default {
    props: ['items'],

}
</script>

<style>
.el-col {
    border-radius: 4px;
}

.searchList {
    margin: 30px auto;
}
</style>