import { defineStore } from "pinia";
import Cookies from "js-cookie";


export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    isLoggedIn: isLogIn(),
    username: "",
  }),
  actions: {
    login() {
      this.isLoggedIn = true;
    },
    signout() {
      this.isLoggedIn = false;
    },
  },
});

function isLogIn() {
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  console.log("isLogIn");
  console.log(access_token_cookie !== undefined);
  return access_token_cookie !== undefined;
}
