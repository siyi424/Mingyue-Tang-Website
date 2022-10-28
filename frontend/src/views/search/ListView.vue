<template>
  <div class="searchList" v-if="isShow">
    <el-row :gutter="20" v-for="item in this.items" :key="item.id" @click="interRoom">
      <el-col :span="3">{{item.name}}</el-col>
      <el-col :span="6">{{item.birth}}</el-col>
      <el-col :span="6">{{item.passDate}}</el-col>
      <el-col :span="3">{{item.gender}}</el-col>
      <el-col :span="6" id="last">{{item.desc}}</el-col>
    </el-row>
  </div>
  <router-view v-else></router-view>
</template>

<script>
import axios from "axios";


export default {
    props: ['name'], 
    data(){
      return {
        items: '',
        isShow: true,
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

      interRoom() {
        this.isShow = false;
        this.$router.push({name:'singleChat', params: {person: this.name}});
      }
    }
}
</script>

<style>
.searchList {
  background: rgba(255, 255, 255, 0.8);
  margin: 60px auto;
  width: 700px;
}

.el-row {
  margin: 30px;
  background: black;
  color: white;
  box-shadow: 0 0 4px black;
  font-size: 30px;
}

.el-row:hover {
  cursor: pointer;
}

#last {
  overflow: auto;
}


</style>