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

export default {
  name: 'Home',
  components: {
    ProductPage
  },
  data() {
    return {
      searchQuery: '',
      products: [
        {
          id: 1,
          name: 'Product 1',
          category: 'Category 1',
          description: 'Description1',
          image: 'https://via.placeholder.com/150',
          price: 10.99,
          sellerId: 1,
          sellerName: 'Seller 1'
        },
        {
          id: 2,
          name: 'Product 2',
          category: 'Category 2',
          description: 'Description2',
          image: 'https://via.placeholder.com/150',
          price: 19.99,
          sellerId: 1,
          sellerName: 'Seller 1'
        },
        {
          id: 3,
          name: 'Product 3',
          category: 'Category 3',
          description: 'Description3',
          image: 'https://via.placeholder.com/150',
          price: 15.99,
          sellerId: 2,
          sellerName: 'Seller 2'
        },
        {
          id: 4,
          name: 'Product 4',
          category: 'Category 4',
          description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
          image: 'https://via.placeholder.com/150',
          price: 8.99,
          sellerId: 2,
          sellerName: 'Seller 2'
        },
        {
        id: 5,
        name: 'Product 5',
        category: 'Category 1',
        description: 'Description4',
        image: 'https://via.placeholder.com/150',
        price: 12.99,
        sellerId: 3,
        sellerName: 'Seller 3'
      },
      {
        id: 6,
        name: 'Product 6',
        category: 'Category 2',
        description: 'Description5',
        image: 'https://via.placeholder.com/150',
        price: 29.99,
        sellerId: 3,
        sellerName: 'Seller 3'
      },
      {
        id: 7,
        name: 'Product 7',
        category: 'Category 3',
        description: 'Description6',
        image: 'https://via.placeholder.com/150',
        price: 17.99,
        sellerId: 4,
        sellerName: 'Seller 4'
      },
      {
        id: 8,
        name: 'Product 8',
        category: 'Category 4',
        description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
        image: 'https://via.placeholder.com/150',
        price: 11.99,
        sellerId: 4,
        sellerName: 'Seller 4'
      },
      {
        id: 9,
        name: 'Product 9',
        category: 'Category 1',
        description: 'Description7',
        image: 'https://via.placeholder.com/150',
        price: 9.99,
        sellerId: 5,
        sellerName: 'Seller 5'
      },
      {
        id: 10,
        name: 'Product 10',
        category: 'Category 2',
        description: 'Description8',
        image: 'https://via.placeholder.com/150',
        price: 24.99,
        sellerId: 5,
        sellerName: 'Seller 5'
      },
      {
      id: 11,
      name: 'Product 11',
      category: 'Category 3',
      description: 'Description9',
      image: 'https://via.placeholder.com/150',
      price: 13.99,
      sellerId: 6,
      sellerName: 'Seller 6'
    },
    {
      id: 12,
      name: 'Product 12',
      category: 'Category 4',
      description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
      image: 'https://via.placeholder.com/150',
      price: 7.99,
      sellerId: 6,
      sellerName: 'Seller 6'
    },
    {
      id: 13,
      name: 'Product 13',
      category: 'Category 1',
      description: 'Description10',
      image: 'https://via.placeholder.com/150',
      price: 18.99,
      sellerId: 7,
      sellerName: 'Seller 7'
    },
    {
      id: 14,
      name: 'Product 14',
      category: 'Category 2',
      description: 'Description11',
      image: 'https://via.placeholder.com/150',
      price: 22.99,
      sellerId: 7,
      sellerName: 'Seller 7'
    },
    {
      id: 15,
      name: 'Product 15',
      category: 'Category 3',
      description: 'Description12',
      image: 'https://via.placeholder.com/150',
      price: 16.99,
      sellerId: 8,
      sellerName: 'Seller 8'
    },
    {
      id: 16,
      name: 'Product 16',
      category: 'Category 4',
      description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
      image: 'https://via.placeholder.com/150',
      price: 9.99,
      sellerId: 8,
      sellerName: 'Seller 8'
    },
    {
      id: 17,
      name: 'Product 17',
      category: 'Category 1',
      description: 'Description13',
      image: 'https://via.placeholder.com/150',
      price: 11.99,
      sellerId: 9,
      sellerName: 'Seller 9'
    },
    {
      id: 18,
      name: 'Product 18',
      category: 'Category 2',
      description: 'Description14',
      image: 'https://via.placeholder.com/150',
      price: 27.99,
      sellerId: 9,
      sellerName: 'Seller 9'
    },
    {
      id: 19,
      name: 'Product 19',
      category: 'Category 3',
      description: 'Description15',
      image: 'https://via.placeholder.com/150',
      price: 14.99,
      sellerId: 10,
      sellerName: 'Seller 10'
    },
    {
      id: 20,
      name: 'Product 20',
      category: 'Category 4',
      description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
      image: 'https://via.placeholder.com/150',
      price: 6.99,
      sellerId: 10,
      sellerName: 'Seller 10'
    },
    {
      id: 21,
      name: 'Product 21',
      category: 'Category 1',
      description: 'Description16',
      image: 'https://via.placeholder.com/150',
      price: 10.49,
      sellerId: 11,
      sellerName: 'Seller 11'
    },
    {
      id: 22,
      name: 'Product 22',
      category: 'Category 2',
      description: 'Description17',
      image: 'https://via.placeholder.com/150',
      price: 23.99,
      sellerId: 11,
      sellerName: 'Seller 11'
    },
    {
      id: 23,
      name: 'Product 23',
      category: 'Category 3',
      description: 'Description18',
      image: 'https://via.placeholder.com/150',
      price: 17.99,
      sellerId: 12,
      sellerName: 'Seller 12'
    },
    {
      id: 24,
      name: 'Product 24',
      category: 'Category 4',
      description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
      image: 'https://via.placeholder.com/150',
      price: 8.49,
      sellerId: 12,
      sellerName: 'Seller 12'
    },
    {
      id: 25,
      name: 'Product 25',
      category: 'Category 1',
      description: 'Description19',
      image: 'https://via.placeholder.com/150',
      price: 12.99,
      sellerId: 13,
      sellerName: 'Seller 13'
    },
    {
      id: 26,
      name: 'Product 26',
      category: 'Category 2',
      description: 'Description20',
      image: 'https://via.placeholder.com/150',
      price: 28.99,
      sellerId: 13,
      sellerName: 'Seller 13'
    },
    {
      id: 27,
      name: 'Product 27',
      category: 'Category 3',
      description: 'Description21',
      image: 'https://via.placeholder.com/150',
      price: 15.99,
      sellerId: 14,
      sellerName: 'Seller 14'
    },
    {
      id: 28,
      name: 'Product 28',
      category: 'Category 4',
      description: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
      image: 'https://via.placeholder.com/150',
      price: 10.49,
      sellerId: 14,
      sellerName: 'Seller 14'
    },
    {
      id: 29,
      name: 'Product 29',
      category: 'Category 1',
      description: 'Description22',
      image: 'https://via.placeholder.com/150',
      price: 14.99,
      sellerId: 15,
      sellerName: 'Seller 15'
    },
    {
      id: 30,
      name: 'Product 30',
      category: 'Category 2',
      description: 'Description23',
      image: 'https://via.placeholder.com/150',
      price: 26.99,
      sellerId: 15,
      sellerName: 'Seller 15'
    }
      ]
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
          product.description.toLowerCase().includes(this.searchQuery.toLowerCase())
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
