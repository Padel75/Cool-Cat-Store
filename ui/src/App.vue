<template>
  <div id="app">
    <nav-menu></nav-menu>
    <router-view></router-view>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
export default {
  name: "app",
  components: {
    "nav-menu": Navigation,
  },
   metaInfo() {
        return {
            meta: [
                { charset: 'utf-8' },
                { equiv: 'Content-Type', content: 'text/html' },
                { name: 'viewport', content: 'width=device-width, initial-scale=1' }

            ]
        }
    },
};
</script>

<style>
.evaluation {
  display: flex;
}

.rating {
  width: 120px;
  height: 24px;
  position: relative;
  margin-right: 10px;
}

.rating progress.rating-bg {
  -webkit-appearance: none;
  -moz-appearence: none;
  appearance: none;
  border: none;
  display: inline-block;
  height: 24px;
  width: 100%;
  color: orange;
}

.rating progress.rating-bg::-webkit-progress-value {
  background-color: orange;
}

.rating progress.rating-bg::-moz-progress-bar {
  background-color: orange;
}

.rating svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
