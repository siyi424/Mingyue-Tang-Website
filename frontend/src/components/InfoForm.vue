<template>
  <el-form :model="form" label-width="120px">
    <!-- name -->
    <el-form-item label="逝者名字">
      <el-input v-model="form.name" />
    </el-form-item>
    <!-- time -->
    <el-form-item label="出生时间">
      <el-date-picker
        v-model="form.date1"
        type="date"
        placeholder="Pick a date"
        format="YYYY/MM/DD"
        value-format="YYYY-MM-DD"
        style="width: 100%"
      />
    </el-form-item>
    <el-form-item label="去世时间">
      <el-date-picker
        v-model="form.date2"
        type="date"
        format="YYYY/MM/DD"
        value-format="YYYY-MM-DD"
        placeholder="Pick a date"
        style="width: 100%"
      />
    </el-form-item>

    <!-- 性别 -->
    <el-form-item label="性别">
      <el-radio-group v-model="form.gender">
        <el-radio label="男" />
        <el-radio label="女" />
      </el-radio-group>
    </el-form-item>
    <!-- 介绍逝者 -->
    <el-form-item label="介绍逝者">
      <el-input v-model="form.desc" type="textarea" />
    </el-form-item>

    <!-- 按钮 -->
    <el-form-item>
      <el-button type="primary" @click="onSubmit">创建</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        name: "",
        date1: "",
        date2: "",
        gender: "",
        desc: "",
      },
    };
  },

  methods: {
    onSubmit() {
      console.log('the form is:', this.form);
      axios.post("/addInfo/register", {
          name: this.form.name,
          date1: this.form.date1,
          date2: this.form.date2,
          gender: this.form.gender,
          desc: this.form.desc,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });

      console.log("succesfully submit!");
    },
  },
};
</script>
