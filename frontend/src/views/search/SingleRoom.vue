<template>
  <div class="chat">
    (调用AI聊天机器人api，进行对话)

    <room-layout>{{person}}</room-layout>
  </div>
</template>

<script>
import RoomLayout from "../../components/RoomLayout.vue"

export default {
    components: {RoomLayout},
    props: ['person'],
}
</script>

<style>
.chat {
    width: 500px;
    margin: 50px auto;
    background: rgba(255, 255, 255, 0.8);
    color: black;
}
</style>