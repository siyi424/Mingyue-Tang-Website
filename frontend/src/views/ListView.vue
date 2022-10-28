<template>
  <div class="searchList" >
    <el-row :gutter="20" v-for="item in this.items" :key="item.id">
      <el-col :span="3">{{item.name}}</el-col>
      <el-col :span="6">{{item.birth}}</el-col>
      <el-col :span="6">{{item.passDate}}</el-col>
      <el-col :span="3">{{item.gender}}</el-col>
      <el-col :span="6">{{item.desc}}</el-col>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";


export default {
    props: ['name'], 
    data(){
      return {
        items: '',
      }
    },
    created() {
      this.searchName();
    },

    watch: {
      items: {
        deep: true,
      }
    },
    methods: {
      searchName() {
      axios
        .get("/addInfo/searchName", {
          params: {
            name: this.name,
          },
        })
        .then((response)=>{
          const data = response.data.getData;
          console.log('GET: ', data);
          this.items = data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    }
}
</script>

<style>
.searchList {
  background: rgba(255, 255, 255, 0.8);
  margin: 30px auto;
  width: 1000px;
}

.el-row {
  margin: 10px 0;
  background: black;
  color: white;
  box-shadow: 0 0 4px black;
  font-size: 30px;
}

.el-col {
    border-radius: 4px;
}

.searchList {
    margin: 30px auto;
}
</style>