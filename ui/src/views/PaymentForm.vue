<template>
  <div class="payment-form">
    <h2 class="form-heading">Select Payment Method</h2>
    <div class="form-group">
      <div>
        <input type="radio" id="creditCard" name="paymentMethod" v-model="selectedPaymentMethod" value="creditCard">
        <label class="form-label" for="creditCard" style="display: inline-block; margin-left: 5px;">Credit Card</label>
      </div>
    </div>
    <div class="form-group">
      <div>
        <input type="radio" id="paypal" name="paymentMethod" v-model="selectedPaymentMethod" value="paypal">
        <label class="form-label" for="paypal" style="display: inline-block; margin-left: 5px;">PayPal</label>
      </div>
    </div>
    <div v-if="selectedPaymentMethod === 'paypal'">
      <div class="form-group">
        <label class="form-label" for="paypalEmail">Email:</label>
        <input class="form-input" type="email" id="paypalEmail" v-model="paypalEmail" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="paypalPassword">Password:</label>
        <input class="form-input" type="password" id="paypalPassword" v-model="paypalPassword" required>
      </div>
    </div>
    <div v-if="selectedPaymentMethod === 'creditCard'">
      <div class="form-group">
        <label class="form-label" for="cardNumber">Card Number:</label>
        <input class="form-input" type="text" id="cardNumber" v-model="cardNumber" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="expiryDate">Expiry Date:</label>
        <input class="form-input" type="text" id="expiryDate" v-model="expiryDate" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="cvv">CVV:</label>
        <input class="form-input" type="text" id="cvv" v-model="cvv" required>
      </div>
    </div>
    <div class="row" style="justify-content: space-between; align-items: center;">
      <b class="cart-total-price" style="margin-right: auto;">Total: {{ this.totalCost }} $ </b>
      <button class="form-button" style="margin-right: auto;" @click="processPayment()">Process Payment</button>

    </div>
    <div class="item-group" style="right: auto;">
      <ul>
        <li v-for="item in cartItems" :key="item.product.id">
          <div class="columns is-vcentered" >
            <div class="column is-6">
              <p class="cart-item-name">{{ item.product.name }}  ( {{ item.quantity }} )  :  {{ item.product.price }}$</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import {getCart} from "@/api/cart";
import {useUserStore} from "@/stores/user";

export default {
  data() {
    return {
      selectedPaymentMethod: 'creditCard',
      paypalEmail: '',
      paypalPassword: '',
      cardNumber: '',
      expiryDate: '',
      cvv: '',
      cartItems: [],
      totalCost: 0,
    };
  },
  mounted() {
      this.fetchCart();
  },
  methods: {
    processPayment() {
      // Use the selected payment method and input fields data to process the payment
      // ...
    },
      fetchCart() {
        const userStore = useUserStore();
        if (userStore.isCustomer){
          getCart().then((response) => {
            this.cartItems = response.data.cart;
            this.totalCost = response.data.total_cost;
          });
        }
      },
  },
};
</script>
<style scoped>
.form-heading {
  margin-top: 0;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.item-group {
  margin-bottom: 20px;
}

.cart-total-price {
  display: block;
  margin-bottom: 5px;
  font-size: 1.2rem;
  color: #333;

}

.cart-item-name {
  font-size: 1.2rem;
  color: #333;
  margin-bottom: 5px;
}
.form-label {
  display: block;
  margin-bottom: 5px;
  font-size: 1.2rem;
  color: #333;
}
.cart-item-quantity {
  font-size: 1rem;
  color: #999;
  margin-bottom: 5px;
}

.cart-item-price {
  font-size: 1.2rem;
  color: #333;
  margin-bottom: 5px;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
  font-size: 1.2rem;
  color: #333;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-input:focus {
  outline: none;
  border-color: #4CAF50;
}

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

.form-button:hover {
  background-color: #3e8e41;
}


.payment-form {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
  background-color: #fff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>

