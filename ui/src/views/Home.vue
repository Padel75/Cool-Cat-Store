<template>
  <div class="home">
    <div class="search">
      <input type="text" v-model="searchQuery" placeholder="Search Products..." />
      <select v-model="selectedCategory" @change="simulateSpaceBackspace">
        <option value="">All Categories</option>
        <option v-for="category in uniqueCategories" :key="category">{{ category }}</option>
      </select>
    </div>
    <ul class="product-list">
      <li v-for="product in displayedProducts" :key="product.id" class="product-list-item">
        <product-page :product="product" />
      </li>
    </ul>
    <div class="pagination">
      <button class="pagination-button" :disabled="currentPage === 1" @click="currentPage--">Previous Page</button>
      <button class="pagination-button" :disabled="currentPage === totalPages" @click="currentPage++">Next Page</button>
    </div>
  </div>
</template>

<script>
import ProductPage from './ProductPage.vue';
import { getProducts } from '@/api/products';

export default {
  name: 'Home',
  components: {
    ProductPage
  },
  data() {
    return {
      searchQuery: '',
      products: getProducts().then(products => {
        this.products = products.data;
        this.totalPages = Math.ceil(this.products.length / this.productsPerPage);
      }),
      currentPage: 1,
      productsPerPage: 10,
      totalPages: 1,
      selectedCategory: ''
    };
  },
  computed: {
    filteredProducts() {
      let filtered = this.products;

      if (this.selectedCategory) {
        filtered = filtered.filter(product => product.category === this.selectedCategory);
      }

      if (this.searchQuery) {
        filtered = filtered.filter(product =>
          product.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          product.category.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }

      return filtered;
    },
    displayedProducts() {
      const startIndex = (this.currentPage - 1) * this.productsPerPage;
      const endIndex = startIndex + this.productsPerPage;

      return this.filteredProducts.slice(startIndex, endIndex);
    },
    uniqueCategories() {
      const categories = this.products.map(product => product.category);
      return Array.from(new Set(categories));
    }
  },
  methods: {
    simulateSpaceBackspace() {
      this.searchQuery += ' ';
      this.$nextTick(() => {
        this.searchQuery = this.searchQuery.trim();
      });
    },
  },
};
</script>

<style scoped>
.home {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
}

.search {
  margin-bottom: 20px;
}

.product-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.product-list-item {
  margin-bottom: 20px;
}

.pagination {
  margin-top: 20px;
}

.pagination button {
  margin-right: 10px;
}
</style>
