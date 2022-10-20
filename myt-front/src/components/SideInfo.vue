<template>
  <el-drawer v-model='drawer2' :direction="direction" z-index=-1>
      <h4>set title by slot</h4>
    
      <div>
        hello!
      </div>
    
      <div style="flex: auto">
        <el-button @click="cancelClick">cancel</el-button>
        <el-button type="primary" @click="confirmClick">confirm</el-button>
      </div>
  </el-drawer>
</template>

<script>
export default {
    data() {
        return {
            direction: 'ltr',
            drawer2: true,
        }
    },
    methods: {
        cancelClick() {
            console.log('function cancel')
        },

        confirmClick() {
            console.log('function confirm')
        }
    }
}
</script>

<style>

</style>