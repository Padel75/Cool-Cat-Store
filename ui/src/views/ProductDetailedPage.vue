<template>
  <div class="product-page">
    <div class="product-header">
      <h1 class="product-name">{{ product.name }}</h1>
      <span class="product-price">{{ product.price }} CAD</span>
    </div>
    <div class="product-body">
      <img :src="product.image" class="product-image" alt="Product Image" />
      <div class="product-details">
        <p class="product-category">{{ product.category }}</p>
        <p class="product-size">{{ product.size }}</p>
        <router-link :to="{ name: 'Seller', params: { id: product.sellerId } }">
          <p class="product-seller">Sold by <span class="product-seller-name">{{ product.sellerName }}</span></p>
        </router-link>
      </div>
    </div>
    <div class="product-footer">
      <button class="add-to-cart-button" @click="addToCart">Add to Cart</button>
      <input class="form-input" type="number" step="1" id="quantity" v-model="quantity" required>
    </div>
  </div>

</template>

<script>
import { getProduct } from '@/api/products';
import { addToCart } from "@/api/cart";

export default {
  name: 'Product',
  data() {
    return {
      product: getProduct(this.$route.params.id).then(product => {
        this.product = product.data;
      }),
      quantity: 1
    };
  },
  methods: {
    addToCart() {
      addToCart(this.product.id, this.quantity);
    }
  }
};
</script>

<style scoped>
.product-page {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
  background-color: #fff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.product-name {
  font-size: 2rem;
  margin-top: 0;
  color: #333;
}

.product-price {
  font-size: 1.5rem;
  font-weight: bold;
  color: #4CAF50;
}

.product-image {
  max-width: 200px;
  height: auto;
  margin-bottom: 20px;
  border-radius: 8px;
}

.product-details {
  margin-top: 20px;
}

.product-category,
.product-size {
  margin: 0;
  color: #555;
}

.product-seller {
  font-size: 1.2rem;
  margin-top: 10px;
  color: #777;
}

.product-seller-name {
  font-weight: bold;
  color: #000;
}

.product-footer {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

#quantity {
  width: 50px;
  margin-right: 10px;
}

.add-to-cart-button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 1.2rem;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease-in-out;
}

.add-to-cart-button:hover {
  background-color: #3e8e41;
}
</style>
