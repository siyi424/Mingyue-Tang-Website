<template>
  <div class="Info">
    <!-- adding the passed person's Info -->
    <div class="Info-left">
      111
    </div>
    <!-- showing the passed info, chatting window -->
    <div class="Info-center">
      111
    </div>
    <!-- persion in this room -->
    <div class="Info-right">
      111
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style>
.Info {
  background: rgba(255,255,255,0.8);
  display: grid;
  padding-top: 40px;
  height: 1000px;
  grid-template-columns: 2fr 3fr 2fr;
  grid-column-gap: 40px;
}

.Info-left, .Info-center, .Info-right {
  background: black;
  height: 1000px;
  border-radius: 5px;
  box-shadow: 0 0 15px black;
}

.Info-left {
  margin-left: 50px;
}

.Info-right {
  margin-right: 50px;
}

</style>
