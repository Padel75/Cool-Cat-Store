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
      <li v-for="product in filteredProducts" :key="product.id" class="product-list-item">
        <product-page :product="product" />
      </li>
    </ul>
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
      }),
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
</style>
