<script setup>
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
const router = useRouter();
const userStore = useUserStore();
const login = () => {
  userStore.login();
  router.push("/");
};
</script>

<template>
  <section class="hero">
    <div class="hero-body has-text-centered">
      <div class="login">
        <h3 class="title has-text-black">Log in</h3>
        <hr class="login-hr" />
        <p class="subtitle has-text-black">Please log in to proceed.</p>
        <div class="box" id="loginBox">
          <form>
            <div class="field">
              <div class="control has-icons-left">
                <input
                  class="input is-medium"
                  type="email"
                  placeholder="Email"
                  autofocus="true"
                />
              </div>
            </div>
            <div class="field">
              <div class="control has-icons-left">
                <input
                  class="input is-medium"
                  type="password"
                  placeholder="Password"
                />
              </div>
            </div>
            <button
              class="button is-block is-info is-medium is-fullwidth"
              @click="login()"
            >
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
#loginBox {
  min-width: 600px;
  max-width: 700px;
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
</style>
