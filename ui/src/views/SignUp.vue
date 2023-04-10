<template>
  <section class="hero">
    <div class="hero-body has-text-centered">
      <div class="login">
        <h3 class="title has-text-black">Sign up</h3>
        <hr class="login-hr" />
        <p class="subtitle has-text-black">Please select your user type:</p>
        <div class="buttons has-addons">
          <router-link class="navbar-item" to="/signup/seller">Seller</router-link>
          <router-link class="navbar-item" to="/signup/customer">Customer</router-link>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
const router = useRouter();
const userStore = useUserStore();

let userType = "customer";

const setUserType = (type) => {
  userType = type;
};

const signUp = () => {
  userStore.login();
  router.push("/");
};
</script>

<style scoped>
#loginBox {
  min-width: 600px;
  max-width: 800px;
  margin: 0 auto;
}
@media screen and (max-width: 560px) {
  #loginBox {
    min-width: 300px;
    max-width: 500px;
  }
}
.hero-body {
  display: flex;
  justify-content: center;
  align-items: flex-start;
}
.login {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 1.5rem;
}
.buttons.has-addons {
  margin-bottom: 1.5rem;
}
.buttons.has-addons .button {
  border-radius: 0;
  border: none;
  transition: background-color 0.2s ease-in-out;
}
.buttons.has-addons .button:hover {
  background-color: #f5f5f5;
}
.buttons.has-addons .button.is-primary {
  background-color: #3273dc;
  color: white;
}
</style>
