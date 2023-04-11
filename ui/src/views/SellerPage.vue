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
import ProductPage from './ProductPage.vue';
import { getSeller } from '@/api/seller';
import { getSellerProducts } from '@/api/products';

export default {
  name: 'Seller',
  components: {
    ProductPage
  },
  data() {
    return {
      seller: {
        name: '',
        description: '',
        products: getSellerProducts(this.$route.params.id).then(response => {
          this.seller.products = response.data;
      }),
      }
    };
  },
  mounted() {
    this.fetchSeller();
  },
  methods: {
    fetchSeller() {
      getSeller(this.$route.params.id)
        .then(response => {
          this.seller.name = response.data.name;
          this.seller.description = response.data.description;
        });
    }
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
  font-size: 3rem;
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
