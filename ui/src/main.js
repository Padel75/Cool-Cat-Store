import { createApp } from "vue";
import { router } from "./router";
import { createPinia } from "pinia";
import App from "./App.vue";
import axios from "axios";
import "../node_modules/mapbox-gl/dist/mapbox-gl.css"
import "../styles/style.css";

const pinia = createPinia();
const app = createApp(App);

axios.defaults.baseURL = "http://localhost:5000";

app.use(router);
app.use(pinia);
app.mount("#app");
