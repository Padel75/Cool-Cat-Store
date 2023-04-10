import { defineStore } from "pinia";

export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    isLoggedIn: false,
    username: "username",
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
