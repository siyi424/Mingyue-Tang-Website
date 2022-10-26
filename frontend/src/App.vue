<template>
  <nav>
    <!-- nav-right -->
    <div class="icon-search" @click="searchName">
      <svg
        t="1666259603147"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="6695"
        width="48"
        height="48"
        data-spm-anchor-id="a313x.7781069.0.i16"
      >
        <path
          d="M953.6 795.733333l-145.066667-192c53.333333-44.8 89.6-113.066667 89.6-187.733333C896 279.466667 787.2 170.666667 650.666667 170.666667 516.266667 170.666667 405.333333 279.466667 405.333333 416S516.266667 661.333333 650.666667 661.333333c44.8 0 85.333333-12.8 121.6-32v2.133334l145.066666 192c4.266667 6.4 10.666667 8.533333 17.066667 8.533333 4.266667 0 8.533333-2.133333 12.8-4.266667 10.666667-8.533333 12.8-23.466667 6.4-32zM448 416c0-110.933333 91.733333-202.666667 202.666667-202.666667s202.666667 91.733333 202.666666 202.666667-91.733333 202.666667-202.666666 202.666667-202.666667-91.733333-202.666667-202.666667zM128 277.333333h192c12.8 0 21.333333-8.533333 21.333333-21.333333s-8.533333-21.333333-21.333333-21.333333H128c-12.8 0-21.333333 8.533333-21.333333 21.333333s8.533333 21.333333 21.333333 21.333333zM128 490.666667c-12.8 0-21.333333 8.533333-21.333333 21.333333s8.533333 21.333333 21.333333 21.333333h128c12.8 0 21.333333-8.533333 21.333333-21.333333s-8.533333-21.333333-21.333333-21.333333H128zM467.2 701.866667h-341.333333c-12.8 0-21.333333 8.533333-21.333334 21.333333s8.533333 21.333333 21.333334 21.333333h341.333333c12.8 0 21.333333-8.533333 21.333333-21.333333s-8.533333-21.333333-21.333333-21.333333z"
          p-id="6696"
          fill="#ffffff"
          data-spm-anchor-id="a313x.7781069.0.i17"
          class="selected"
        ></path>
      </svg>
    </div>

    <div>
      <el-input id="search" v-model="inputName" placeholder="搜索逝者名字" @change="searchName"/>
    </div>
    <!-- nav-left  -->
    <div class="nav-left">
      <!-- home  -->
      <router-link to="/"
        ><svg
          t="1666344612143"
          id="icon-home"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="5425"
          width="32"
          height="32"
        >
          <path
            d="M946.488889 505.002667l-411.875556-411.591111a31.914667 31.914667 0 0 0-45.226666 0l-411.875556 411.591111c-12.003556 12.003556-18.830222 28.302222-18.830222 45.283555a64.056889 64.056889 0 0 0 64 64H166.115556v293.717334c0 17.692444 14.307556 32 32 32h249.912888v-224h111.985778v224h265.898667c17.720889 0 32-14.307556 32-32V614.286222h43.406222a64.056889 64.056889 0 0 0 45.226667-109.283555z"
            p-id="5426"
            fill="#ffffff"
          ></path></svg
      ></router-link>
      |
      <!-- rightarrow -->
      <router-link to="/info"
        ><svg
          t="1666271128973"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="9310"
          width="48"
          height="48"
        >
          <path
            d="M393.151172 263.251659c-12.489452 12.489452-12.489452 32.737612 0 45.227064L596.673471 512 393.151172 715.521277c-12.489452 12.489452-12.489452 32.737612 0 45.227064 12.489452 12.489452 32.737612 12.489452 45.227064 0l226.13532-226.135321c12.489452-12.489452 12.489452-32.737612 0-45.227064L438.378236 263.251659c-12.488429-12.489452-32.737612-12.489452-45.227064 0z"
            p-id="9311"
            fill="#ffffff"
          ></path></svg
      ></router-link>
      <!-- verticle line  -->
      <svg
        t="1666345076703"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="6710"
        width="48"
        height="48"
      >
        <path
          d="M474.91 67h74.19v890h-74.19z"
          p-id="6711"
          fill="#8a8a8a"
        ></path>
      </svg>
      <!-- audio music  -->
      <audio
        controls
        loop
        id="bgmusic"
        autoplay="autoplay"
        src="/media/music.m4a"
      ></audio>
    </div>
  </nav>

  <!-- render-place  -->
  <router-view />
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      inputName: "",
      items: undefined,
    }
  },
  methods: {
    searchName() {
      console.log("inputName: ", this.inputName);
      axios
        .get("/addInfo/searchName", {
          params: {
            name: this.inputName,
          },
        })
        .then((response)=>{
          this.items = response.data.getData;
          console.log(response.data.getData);
        })
        .catch(function (error) {
          console.log(error);
        })
        .then(function () {
          // 总是会执行
        });

        this.$router.push('/search', this.items);
        console.log('GET succesfully!');
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  border: 0;
  outline: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background: black;
  height: 1400px;
}

nav {
  padding: 20px 40px;
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  box-shadow: 0 0 10px white;
}

.nav-left {
  margin-right: auto;
}

.icon-search {
  margin-top: 5px;
  margin-right: 30px;
  margin-left: 20px;
}
.icon-search:hover {
  cursor: pointer;
}

#search {
  height: 35px;
  width: 300px;
  border-radius: 5px;
  box-shadow: 0 0 3px rgba(255, 255, 255, 0.9);
  font-size: 100%;
}

#icon-home {
  margin-bottom: 6px;
}

#bgmusic {
  margin: 0 20px;
  padding: 10px;
}
</style>
