import axios from 'axios';
import { useUserStore } from "@/stores/user";
import { router } from "@/router";
// import { useRouter } from "vue-router";
//
// const router = useRouter()
const userStore = useUserStore();

export function login(username, password) {
  const url = `${axios.defaults.baseURL}/login`;
  const data = {
    username: username,
    password: password
  };
  axios.post(url, data)
    .then(response => {
      if (response.status === 200) {
            userStore.login();
            console.log("Logged in");
            router.push('/home'); //confirmer où on veut rediriger
            console.log("Redirected");
          }
    })
    .catch(error => {
      console.log(error);
      if (error.response.status === 400) {
        alert("Wrong username or password");
      }
      else {
        alert("Something went wrong");
      }
    });
}
