<template>
  <div class="product-form">
    <h2 class="form-heading">Add New Product</h2>
    <form class="form" @submit.prevent="handleSubmit">
      <div class="form-group">
        <label class="form-label" for="name">Name:</label>
        <input class="form-input" type="text" id="name" v-model="product.name" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="category">Category:</label>
        <input class="form-input" type="text" id="category" v-model="product.category" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="description">Description:</label>
        <textarea class="form-input" id="description" v-model="product.description" required></textarea>
      </div>
      <div class="form-group">
        <label class="form-label" for="price">Price:</label>
        <input class="form-input" type="number" step="0.01" id="price" v-model="product.price" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="image">Image URL:</label>
        <input class="form-input" type="url" id="image" v-model="product.image" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="sellerId">Seller ID:</label>
        <input class="form-input" type="text" id="sellerId" v-model="product.sellerId" required>
      </div>
      <div class="form-group">
        <label class="form-label" for="sellerName">Seller Name:</label>
        <input class="form-input" type="text" id="sellerName" v-model="product.sellerName" required>
      </div>
      <button class="form-button" type="submit">Add Product</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ProductForm',
  data() {
    return {
      product: {
        name: '',
        category: '',
        description: '',
        price: null,
        image: '',
        sellerId: null,
        sellerName: ''
      }
    };
  },
  methods: {
    handleSubmit() {
      // Do something with the submitted product data
      console.log(this.product);
      // Reset the form
      this.product = {
        name: '',
        category: '',
        description: '',
        price: null,
        image: '',
        sellerId: null,
        sellerName: ''
      };
    }
  }
};
</script>

<style scoped>
.form-heading {
  margin-top: 0;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.form {
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

.form-button:disabled {
  background-color: #ddd;
  color: #666;
  cursor: not-allowed;
}

.form-button:disabled:hover {
  background-color: #ddd;
}

.product-form {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
  background-color: #fff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}
</style>
