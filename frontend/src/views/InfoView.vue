<template>
  <div class="Info">
    <!-- adding the passed person's Info -->
    <div class="Info-left">
      <info-form></info-form>
    </div>
  </div>
</template>

<script>
import InfoForm from '@/components/InfoForm.vue'



export default {
  components: { InfoForm },

}
</script>

<style>
.Info {
  background: rgba(255,255,255,0.8);
  padding-top: 40px;
  height: 1000px;
}

.Info-left, .Info-center, .Info-right {
  background: black;
  height: 500px;
  border-radius: 5px;
  box-shadow: 0 0 15px black;
}

.Info-left {
  margin: 40px 35%;
  padding-top:50px;
  padding-right: 50px;
}

.Info-right {
  margin-right: 50px;
}


</style>
