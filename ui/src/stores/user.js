import { defineStore } from "pinia";
import Cookies from "js-cookie";


export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    isLoggedIn: isLogIn(),
    username: "",
    isCustomer: isCustomer(),
    isSeller: isSeller(),
  }),
  actions: {
    login() {
      this.isLoggedIn = true;
      this.isCustomer = isCustomer();
      this.isSeller = isSeller();
    },
    signout() {
      this.isLoggedIn = false;
      this.isCustomer = false;
      this.isSeller = false;
    },
  },
});

function isLogIn() {
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  console.log("isLogIn");
  console.log(access_token_cookie !== undefined);
  return access_token_cookie !== undefined;
}

function isCustomer() {
  const role_cookie = document.cookie.split('; ').find(row => row.startsWith('role'));
  console.log("isCustomer");
  console.log(role_cookie !== undefined && role_cookie.split('=')[1] === "customer");
  return role_cookie !== undefined && role_cookie.split('=')[1] === "customer";
}

function isSeller() {
  const role_cookie = document.cookie.split('; ').find(row => row.startsWith('role'));
  console.log("isSeller");
  console.log(role_cookie !== undefined && role_cookie.split('=')[1] === "seller");
  return role_cookie !== undefined && role_cookie.split('=')[1] === "seller";
}
