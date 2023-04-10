<template>
  <div class="customer-form">
    <h2 class="form-heading">Sign up as a Customer</h2>
    <form @submit.prevent="signUp">
      <div class="form-group">
        <label for="userName">User Name:</label>
        <input type="text" id="userName" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password :</label>
        <input type="text" id="password" v-model="password" required>
      </div>
      <div class="form-group">
        <label for="firstName">First Name:</label>
        <input class="form-input" type="text" id="firstName" v-model="first_name" required>
      </div>
      <div class="form-group">
        <label for="lastName">Last Name:</label>
        <input class="form-input" type="text" id="lastName" v-model="last_name" required>
      </div>
      <div class="form-group">
        <label for="phoneNumber">Phone Number:</label>
        <input class="form-input" type="tel" id="phoneNumber" v-model="phone_number" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input class="form-input" type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="address">Address:</label>
        <textarea class="form-input" id="address" v-model="address" required></textarea>
      </div>
      <button type="submit" @click="signUp">Create Customer</button>
    </form>
  </div>
</template>

<script>
import {signUpCustomer} from "@/api/signup";

export default {
  name: 'CustomerForm',
  data: function() {
    return {
      username:"",
      password:"",
      first_name:"",
      last_name:"",
      email:"",
      address:"",
      phone_number:""
    }
  },
  methods: {
    signUp: async function() {
      // create a new customer object using form data
      const response = await signUpCustomer(
        this.username,
        this.password,
        this.first_name,
        this.last_name,
        this.email,
        this.address,
        this.phone_number
    );
        console.log("response");
        console.log(response);
        if (response.status === 201) {
          this.$emit("success-signup");
           console.log("success-signup");
          this.$router.push("/login");
        } else {
          this.$router.push("/signup/customer");
        }
      }
    }
  }
</script>

<style scoped>
.customer-form {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
  background-color: #fff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.form-heading {
  font-size: 2rem;
  margin-top: 0;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #555;
}

input[type="text"],
input[type="tel"],
input[type="email"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  font-size: 1.2rem;
  color: #555;
}

button[type="submit"] {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  border-radius: 4px;
  transition: all 0.3s ease-in-out;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}

button[type="submit"]:disabled {
  background-color: #ddd;
  color: #666;
  cursor: not-allowed;
}

button[type="submit"]:disabled:hover {
  background-color: #ddd;
}
</style>
