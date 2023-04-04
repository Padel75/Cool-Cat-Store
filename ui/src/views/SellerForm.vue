<template>
    <div class="seller-form">
      <h2 class="form-heading">Sign up as a Seller</h2>
      <form @submit.prevent="createSeller">
        <div class="form-group">
          <label for="sellerName">Seller Name:</label>
          <input type="text" id="sellerName" v-model="name" required>
        </div>
        <div class="form-group">
          <label for="sellerDesc">Seller Description:</label>
          <textarea id="sellerDesc" v-model="description" required></textarea>
        </div>
        <div class="form-group">
          <label for="sellerImg">Seller Image URL:</label>
          <input type="text" id="sellerImg" v-model="image" required>
        </div>
        <div class="form-group">
          <label for="sellerAddress">Address:</label>
          <input type="text" id="sellerAddress" v-model="address" required>
        </div>
        <div class="form-group">
          <label for="sellerEmail">Email:</label>
          <input type="email" id="sellerEmail" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="sellerPhone">Phone Number:</label>
          <input type="tel" id="sellerPhone" v-model="phone" required>
        </div>
        <button type="submit">Create Seller</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Seller',
    data() {
      return {
        name: '',
        description: '',
        image: '',
        address: '',
        email: '',
        phone: ''
      }
    },
    methods: {
      createSeller() {
        // create a new seller object using form data
        const newSeller = {
          name: this.name,
          description: this.description,
          image: this.image,
          address: this.address,
          email: this.email,
          phone: this.phone,
          products: []
        };
  
        // send POST request to API to create new seller
        axios.post('/api/sellers', newSeller)
          .then(response => {
            // navigate to newly created seller page
            this.$router.push({ name: 'SellerPage', params: { id: response.data.id } });
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  }
  </script>
  
  <style scoped>
  .seller-form {
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
  