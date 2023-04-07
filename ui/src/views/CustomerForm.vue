<template>
  <div class="customer-form">
    <h2 class="form-heading">Sign up as a Customer</h2>
    <form @submit.prevent="createCustomer">
      <div class="form-group">
        <label for="firstName">First Name:</label>
        <input class="form-input" type="text" id="firstName" v-model="firstName" required>
      </div>
      <div class="form-group">
        <label for="lastName">Last Name:</label>
        <input class="form-input" type="text" id="lastName" v-model="lastName" required>
      </div>
      <div class="form-group">
        <label for="phoneNumber">Phone Number:</label>
        <input class="form-input" type="tel" id="phoneNumber" v-model="phoneNumber" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input class="form-input" type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="address">Address:</label>
        <textarea class="form-input" id="address" v-model="address" required></textarea>
      </div>
      <button class="form-button" type="submit" :disabled="isSubmitting">{{ isSubmitting ? 'Creating Customer...' : 'Create Customer' }}</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CustomerForm',
  data() {
    return {
      firstName: '',
      lastName: '',
      phoneNumber: '',
      email: '',
      address: '',
      isSubmitting: false
    }
  },
  methods: {
    createCustomer() {
      // create a new customer object using form data
      const newCustomer = {
        firstName: this.firstName,
        lastName: this.lastName,
        phoneNumber: this.phoneNumber,
        email: this.email,
        address: this.address
      };

      // send POST request to API to create new customer
      this.isSubmitting = true;
      axios.post('/api/customers', newCustomer)
        .then(response => {
          // navigate to newly created customer page
          this.$router.push({ name: 'CustomerPage', params: { id: response.data.id } });
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => {
          this.isSubmitting = false;
        });
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
