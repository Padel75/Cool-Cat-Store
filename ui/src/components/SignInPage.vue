<template>
  <div class="signin-page">
    <h1>Sign In Informations</h1>
    <form @submit.prevent="saveSignIn" class="signin-form">
      <div class="form-group">
        <label for="email">Email: <span v-if="savedSignIn.email">{{ savedSignIn.email }}</span></label>
        <input type="email" id="email" v-model="signin.email" >
        </div>
      <div class="form-group">
        <label for="password">Password: <span v-if="savedSignIn.password">{{ savedSignIn.password }}</span></label>
        <input type="password" id="password" v-model="signin.password" >
        </div>
      <button type="submit" class="submit-button">Submit login attempt</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignInForm',
  data() {
    return {
      signin: {
        email: '',
        password: ''
      },
      savedSignIn: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    saveSignIn() {
      // Save signin data to backend here
      console.log(this.signin);
      
      // Store the saved signin data in the savedSignIn object
      this.savedSignIn = { ...this.signin };

      let email = this.savedSignIn.email;
      let password = this.savedSignIn.password ;
      
      // Reset form after save to saved
      this.signin.email = email;
      this.signin.password = password ;
    }
  }
}
</script>

<style>
.signin-page {
  max-width: 800px;
  margin: 0 auto;
}

.signin-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-group {
  display: flex;
  flex-direction: column;
  text-align: left;
  gap: 5px;
}

label {
  text-align: left;
  font-weight: bold;
}


input, textarea {
  padding: 5px;
  font-size: 16px;
  width: 50%;
  border
: 1px solid #ccc;
}

.submit-button {
  background-color: #0077cc;
  width: 50%;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.submit-button:hover {
  width: 50%;
  background-color: #0060a3;
}
</style>
