<template>
  <div class="seller-page">
    <div class="seller-header">
      <h1 class="seller-name">{{ seller.name }}</h1>
      <p class="seller-description">{{ seller.description }}</p>
    </div>
    <div class="seller-body">
      <h2 class="product-list-heading">Products</h2>
      <ul class="product-list">
        <li v-for="product in seller.products" :key="product.id" class="product-list-item">
          <product-page :product="product"></product-page>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ProductPage from './ProductPage.vue';

export default {
  name: 'Seller',
  components: {
    ProductPage
  },
  data() {
    return {
      seller: {
        name: 'Dummy Seller',
        description: 'Seller selling description.',
        products: [
          {
            id: 1,
            name: 'Product 1',
            category: 'Category 1',
            description: 'Description product 1',
            price: 10.99,
            image: 'https://via.placeholder.com/150',
            sellerId: 1,
            sellerName: 'Seller 1'
          },
          {
            id: 2,
            name: 'Product 2',
            category: 'Category 2',
            description: 'Description product 2',
            price: 14.99,
            image: 'https://via.placeholder.com/150',
            sellerId: 1,
            sellerName: 'Seller 1'
          },
          {
            id: 3,
            name: 'Product 3',
            category: 'Category 3',
            description: 'Description product 3',
            price: 19.99,
            image: 'https://via.placeholder.com/150',
            sellerId: 1,
            sellerName: 'Seller 1'
          }
        ]
      }
    };
  },
  mounted() {
    // fetch seller data from API and update seller object
    // example using axios library
    /** axios
      .get(`/api/sellers/${this.$route.params.id}`)
      .then(response => {
        this.seller = response.data;
      })
      .catch(error => {
        console.log(error);
      });
    */
  }
};
</script>

<style scoped>
.seller-page {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
}

.seller-name {
  margin-top: 0;
}

.seller-description {
  margin-bottom: 20px;
}

.product-list-heading {
  margin-top: 0;
}

.product-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.product-list-item {
  margin-bottom: 20px;
  border: 1px solid #ddd;
  padding: 20px;
}

.product-image {
  max-width: 
 150px;
    margin-right: 20px;
  }
  
  .product-details {
    flex: 1;
  }
  
  .product-name {
    margin-top: 0;
  }
  
  .product-price {
    font-weight: bold;
    font-size: 1.2rem;
  }
  </style>
  