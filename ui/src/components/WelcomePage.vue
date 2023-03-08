<template>
  <div class="welcome-page">
    <h1>Welcome to our website!</h1>
    <p>Click the button below to go to the customer form page.</p>
    <button @click="goToCustomerPage">To Customer Form</button>
  </div>
</template>

<script>
export default {
  name: 'WelcomePage',
  methods: {
    goToCustomerPage() {
      this.$router.push('/customer-page');
    }
  }
}
</script>

<style>
.welcome-page {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

button {
  background-color: #0077cc;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

button:hover {
  background-color: #0060a3;
}
</style>
