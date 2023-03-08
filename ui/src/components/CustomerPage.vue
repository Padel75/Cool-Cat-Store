
<template>
  <div class="customer-page">
    <h1>Customer Informations</h1>
    <form @submit.prevent="saveCustomer" class="customer-form">
      <div class="form-group">
        <label for="username">User Name: <span v-if="savedCustomer.userName"> {{ savedCustomer.userName }}</span></label>
        <input type="text" id="username" v-model="customer.userName" >
      </div> 
      <div class="form-group">
        <label for="first-name">First Name: <span v-if="savedCustomer.firstName"> {{ savedCustomer.firstName }}</span></label>
        <input type="text" id="first-name" v-model="customer.firstName" >
      </div>
      <div class="form-group">
        <label for="last-name">Last Name: <span v-if="savedCustomer.lastName">{{ savedCustomer.lastName }}</span></label>
        <input type="text" id="last-name" v-model="customer.lastName" >
      </div>
      <div class="form-group">
        <label for="phone-number">Phone Number: <span v-if="savedCustomer.phoneNumber">{{ savedCustomer.phoneNumber }}</span></label>
        <input type="tel" id="phone-number" v-model="customer.phoneNumber" >
      </div>
      <div class="form-group">
        <label for="email">Email: <span v-if="savedCustomer.email">{{ savedCustomer.email }}</span></label>
        <input type="email" id="email" v-model="customer.email" >
        </div>
      <div class="form-group">
        <label for="address">Address: <span v-if="savedCustomer.address">{{ savedCustomer.address }}</span></label>
        <textarea id="address" v-model="customer.address" ></textarea>
        </div>
      <button type="submit" class="submit-button">Save Changes</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CustomerForm',
  data() {
    return {
      customer: {
        userName:'',
        firstName: '',
        lastName: '',
        phoneNumber: '',
        email: '',
        address: ''
      },
      savedCustomer: {
        userName:'',
        firstName: '',
        lastName: '',
        phoneNumber: '',
        email: '',
        address: ''
      }
    }
  },
  methods: {
    async saveCustomer() {
      try{
      // Save customer data to backend here
        console.log(this.customer);
      
      // Store the saved customer data in the savedCustomer object
        this.savedCustomer = { ...this.customer };

        let userName = this.savedCustomer.userName;
        let firstName = this.savedCustomer.firstName;
        let lastName = this.savedCustomer.lastName;
        let phoneNumber = this.savedCustomer.phoneNumber;
        let email = this.savedCustomer.email;
        let address = this.savedCustomer.address ;
      
        // Reset form after save to saved
        this.customer.userName = userName;
        this.customer.firstName = firstName;
        this.customer.lastName = lastName;
        this.customer.phoneNumber = phoneNumber;
        this.customer.email = email;
        this.customer.address = address ;
    } catch (error) {
        console.error(error); // log error message
      }
    }
  }
}
</script>

<style>
.customer-page {
  max-width: 800px;
  margin: 0 auto;
}

.customer-form {
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
