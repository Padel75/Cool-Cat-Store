<template>
  <div class="user-page">
    <div class="user-page-header has-text-centered">
      <h2 class="user-page-title">My account</h2>
    </div>
    <div class="user-header has-text-centered">
      <h1 class="user-name" v-if="user.name">{{ user.name }}</h1>
      <h1 class="user-name" v-else-if="user.first_name && user.last_name">{{ user.first_name }} {{user.last_name}}</h1>
      <p class="user-description" v-if="user.description">{{ user.description }}</p>
      <div class="seller-page-link seller-link" v-if="user.description">
        <router-link :to="{ name: 'Seller', params: { id: user.id } }"  class="button">Go to my public seller page</router-link>
      </div>
      <div class="sell-product-link seller-link" v-if="user.description">
        <router-link to="/product"  class="button">Sell a new product</router-link>
      </div>
    </div>
    <div class="user-body" v-if="user.email && user.phone_number && user.address">
      <h3 class="user-infos-heading">My informations</h3>
      <div class="user-infos">
        <p class="user-infos-item">Email: {{ user.email }}</p>
        <p class="user-infos-item">Phone: {{ user.phone_number }}</p>
        <p class="user-infos-item">Address: {{ user.address }}</p>
      </div>
    </div>
    <div style="margin-top: 10px; margin-bottom: 10px;" v-if="user.first_name">
        <router-link class="form-button" to="/purchases" >View Purchase History</router-link>
      </div>
    <payment-system-form v-if="user.first_name"> </payment-system-form>
  </div>
</template>

<script>
import { getUser } from '@/api/user';
import PaymentSystemForm from './PaymentSystemForm.vue';

export default {
  name: 'User',
  components: {
    PaymentSystemForm
  },
  data() {
    return {
      user: getUser().then(response => {
        this.user = response.data;
      }),
    };
  },
};
</script>

<style scoped>
.form-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  border-radius: 4px;
  transition: all 0.3s ease-in-out;

  }

.user-page {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
}

.user-page-header {
  margin-bottom: 20px;
}

.user-page-title{
  font-size: 3rem;
}

.user-name {
  margin-top: 0;
  font-size: 4rem;
}

.user-description {
  margin-bottom: 20px;
}

.user-infos-heading {
  font-size: 1.5em;
}

.seller-link {
  margin-top: 10px;
}

.user-body{
  margin-top: 50px;
  background-color: #d3d3d3;
  padding: 10px;
}

.user-infos{
  margin-top: 10px;
}

  </style>
