<template>
  <div class="payment-form">
    <h2 class="form-heading">Payment Method</h2>
    <div class="form-group">
      <div>
        <input type="radio" id="Amex" name="paymentMethod" v-model="selectedPaymentMethod" value="Amex" :checked="selectedPaymentMethod=='AMEX'">
        <label class="form-label" for="Amex" style="display: inline-block; margin-left: 5px;">American Express</label>
      </div>
    </div>
    <div class="form-group">
      <div>
        <input type="radio" id="Mastercard" name="paymentMethod" v-model="selectedPaymentMethod" value="Mastercard" :checked="selectedPaymentMethod=='MASTERCARD'">
        <label class="form-label" for="Mastercard" style="display: inline-block; margin-left: 5px;">Master Card</label>
      </div>
    </div>
    <div class="form-group">
      <div>
        <input type="radio" id="Visa" name="paymentMethod" v-model="selectedPaymentMethod" value="Visa" :checked="selectedPaymentMethod=='VISA'">
        <label class="form-label" for="Visa" style="display: inline-block; margin-left: 5px;">Visa</label>
      </div>
    </div>
    <div >
      <div class="form-group">
        <label class="form-label" for="cardNumber">Card Number:</label>
        <input class="form-input" type="text" id="cardNumber" v-model="cardNumber" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="expiryDate">Expiry Date:</label>
        <div class="expiry-date-inputs">
          <input class="form-input" type="text" id="expiryMonth" v-model="expiryMonth" required>
          <span class="date-separator" style="margin-left: 10px; margin-right: 10px"> /</span>
          <input class="form-input" type="text" id="expiryYear" v-model="expiryYear" required>
        </div>
      </div>
      <div class="form-group">
        <label class="form-label" for="cvv">CVV:</label>
        <input class="form-input" type="text" id="cvv" v-model="cvv" required>
      </div>
    </div>
    <button class="form-button" @click="confirmPaymentSystem()">Confirm informations</button>
  </div>
</template>


<script>
import {addPaymentSystem, getPaymentSystem} from "@/api/payment";

export default {
  data() {
    return {
      selectedPaymentMethod: 'creditCard',
      paypalEmail: '',
      paypalPassword: '',
      cardNumber: '',
      expiryMonth: '',
      expiryYear: '',
      cvv: '',
      cartItems: [],
      totalCost: 0,
    };
  },
  mounted() {
    this.fetchPaymentSystem();
  },
  methods: {
    fetchPaymentSystem() {
        getPaymentSystem().then(response => {
          const paymentSystem = response.data[0];
          console.log(paymentSystem)
          this.selectedPaymentMethod = paymentSystem.type;
          this.cardNumber = paymentSystem.number;
          this.cvv = paymentSystem.cvv;
          const expiryDate = new Date(paymentSystem.expiration_date);
          console.log(expiryDate)
          this.expiryYear = expiryDate.getFullYear().toString().slice(-2);
          const expMonth = expiryDate.getMonth() + 1;
          this.expiryMonth = expMonth.toString().length === 1 ? "0" + expMonth.toString() : expMonth.toString();
          console.log(this.selectedPaymentMethod, this.cardNumber, this.cvv, this.expiryMonth, this.expiryYear)
        });
    },
      confirmPaymentSystem() {
        const paymentMethod = this.selectedPaymentMethod;
        const cardNumber = this.cardNumber.toString().replace(/\s/g, '');
        this.expiryMonth = this.expiryMonth.length === 1 ? "0" + this.expiryMonth : this.expiryMonth;
        const yearPrefix = this.expiryYear.length === 2 ? "20" : "";
        const expiryDate = new Date(yearPrefix + this.expiryYear, this.expiryMonth - 1, 1);
        const currentDate = new Date();
        const cvv = this.cvv.replace(/\s/g, '');
        const cvvRegex = /^\d{3}$/;

        let isValid = true;
        console.log(paymentMethod, cardNumber, expiryDate, cvv)

        if (paymentMethod === 'Amex') {
          isValid = /^3\d{15}$/.test(cardNumber);
        } else if (paymentMethod === 'Mastercard') {
          isValid = /^5\d{15}$/.test(cardNumber);
        } else if (paymentMethod === 'Visa') {
          isValid = /^4\d{15}$/.test(cardNumber);
        }
        if (!isValid) {
          alert('Invalid card number for selected payment method.');
          return;
        }

        if (expiryDate <= currentDate) {
          alert('Invalid expiry date.');
          return;
        }
         if (!cvvRegex.test(cvv)) {
            alert('Invalid CVV.');
            return;
          }
         const expiryDateFormatted = `20${this.expiryYear}-${this.expiryMonth}-01`
         addPaymentSystem(paymentMethod, cardNumber, expiryDateFormatted, cvv)
           .then(response => {
             alert('Payment system added successfully.');
           })
      },
  },
};
</script>


<style scoped>

.expiry-date-inputs {
  display: flex;
  align-items: center;
  width:30%;
}

.expiry-date-inputs > * {
  display: inline-block;
  width:30%;
}
.form-heading {
  margin-top: 0;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
    width:50%;
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
}
</style>
