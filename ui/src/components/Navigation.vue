<script setup>
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
import { computed } from "vue";
import CartModal from "../views/CartModal.vue";
import {signOut} from "@/api/signout";
import { ref } from "vue"
const router = useRouter();
const userStore = useUserStore();
const showCartModal = ref(false);
const signout = () => {
  console.log("signedout")
  signOut()
  userStore.signout();
  router.push("/login");
};
const isNotHome = computed(() => {
  return router.currentRoute.value.path != "/";
});
</script>

<template>
  <nav class="navbar has-shadow" role="navigation" aria-label="main navigation">


    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/home"
          >> Home</router-link
        >
        <router-link class="navbar-item" to="/product"
          >+ Product</router-link
        >
        <router-link class="navbar-item" to="/seller"
          >+ Seller</router-link
        >
        <router-link class="navbar-item" to="/customer">+ Customer</router-link>

        <div class="navbar-item">
          <button class="button" v-show="userStore.isLoggedIn" @click="showCartModal = true">
            <h1 class="fas fa-shopping-cart">View Cart</h1>
          </button>
        </div>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link
              v-show="!userStore.isLoggedIn"
              class="button is-light"
              to="/login"
            >
              Log in
            </router-link>
            <router-link
              v-show="!userStore.isLoggedIn"
              class="button is-primary"
              to="/signup"
            >
              Sign-up
            </router-link>

            <a
              class="button is-light"
              v-show="userStore.isLoggedIn"
              @click="signout()"
            > Sign out
            </a>
          </div>
        </div>
      </div>
    </div>
    <CartModal :showModal="showCartModal" @close="showCartModal = false" />
  </nav>
</template>

<style scoped>
#logo-text {
  font-size: 2rem;
}
.navbar{
  position: static;
}
.navbar-burger{
  align-self: center;
}
</style>
