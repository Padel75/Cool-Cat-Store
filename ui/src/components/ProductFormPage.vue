<template>
  <div class="product-form-page">
    <h1>Product Informations</h1>
    <form @submit.prevent="saveProduct" class="product-form">
      <div class="form-group">
        <label for="product-id">Product ID: <span v-if="savedProduct.productId">{{ savedProduct.productId }}</span></label>
        <input type="text" id="product-id" v-model="product.productId" >
        </div>
      <div class="form-group">
        <label for="product-name">Product Name: <span v-if="savedProduct.productName">{{ savedProduct.productName }}</span></label>
        <input type="text" id="product-name" v-model="product.productName" >
        </div>
      <div class="form-group">
        <label for="product-price">Product Price: <span v-if="savedProduct.productPrice">{{ savedProduct.productPrice }}</span></label>
        <input type="tel" id="product-price" v-model="product.productPrice" >
        </div>
      <div class="form-group">
        <label for="category">Category: <span v-if="savedProduct.category">{{ savedProduct.category }}</span></label>
        <input type="category" id="category" v-model="product.category" >
        </div>
      <div class="form-group">
        <label for="description">Description: <span v-if="savedProduct.description">{{ savedProduct.description }}</span></label>
        <textarea id="description" v-model="product.description" ></textarea>
        </div>
      <button type="submit" class="submit-button">Save Changes</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ProductForm',
  data() {
    return {
      product: {
        productId: '',
        productName: '',
        productPrice: '',
        category: '',
        description: ''
      },
      savedProduct: {
        productId: '',
        productName: '',
        productPrice: '',
        category: '',
        description: ''
      }
    }
  },
  methods: {
    saveProduct() {
      // Save product data to backend here
      console.log(this.product);
      
      // Store the saved product data in the savedProduct object
      this.savedProduct = { ...this.product };

      let productId = this.savedProduct.productId;
      let productName = this.savedProduct.productName;
      let productPrice = this.savedProduct.productPrice;
      let category = this.savedProduct.category;
      let description = this.savedProduct.description ;
      
      // Reset form after save to saved informations
      this.product.productId = productId;
      this.product.productName = productName;
      this.product.productPrice = productPrice;
      this.product.category = category;
      this.product.description = description ;
    }
  }
}
</script>

<style>
.product-form-page {
  max-width: 800px;
  margin: 0 auto;
}

.product-form {
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
