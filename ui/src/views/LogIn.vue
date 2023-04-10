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
                  type="text"
                  placeholder="Username"
                  autofocus="true"
                  v-model="username" require
                />
              </div>
            </div>
            <div class="field">
              <div class="control has-icons-left">
                <input
                  class="input is-medium"
                  type="password"
                  placeholder="Password"
                  v-model="password" required
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

<script>
import { logIn } from "../api/login"
import { useRouter } from "vue-router";
const router = useRouter();
import { useUserStore } from "@/stores/user";
const userStore = useUserStore();

export default {
  name: 'LogIn',
  data: function() {
    return {
      username:"",
      password:"",
    }
  },
  methods: {
    login: async function() {
      const response = await logIn(
        this.username,
        this.password,
      );
      console.log("response");
      console.log(response);
      if (response.status === 200) {
        this.$emit("success-login");
        userStore.login()
        userStore.username = this.username
        this.$router.push({ path: "/home" });
      } else {
        alert("Wrong credentials");
      }
    }
  }
}
</script>

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
