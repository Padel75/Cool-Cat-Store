<template>
    <div class="modal" :class="{ 'is-active': showModal }">
      <div class="modal-background" @click="closeModal()"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Shopping Cart</p>
          <button class="delete" aria-label="close" @click="closeModal()"></button>
        </header>
        <section class="modal-card-body">
          <ul>
            <li v-for="item in cartItems" :key="item.id">
              <div class="columns is-vcentered">
                <div class="column is-3">
                  <img :src="item.image" :alt="item.name" class="cart-item-image">
                </div>
                <div class="column is-6">
                  <p class="cart-item-name">{{ item.name }}</p>
                  <p class="cart-item-price">$ {{ item.price }}</p>
                  <p class="cart-item-quantity">qty: {{ item.quantity }}</p>
                </div>
                <div class="column is-3">
                  <button class="delete is-large" aria-label="remove item" @click="removeItem(item)"></button>
                </div>
              </div>
            </li>
          </ul>
          <p class="cart-total-price">Total: {{ cartTotal }}</p>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-danger">Checkout</button>
        </footer>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "CartModal",
    props: {
      showModal: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        cartItems: [
          {
            id: 1,
            name: "Product 1",
            price: 10,
            image: "https://via.placeholder.com/150",
            quantity: 1, 
          },
          {
            id: 2,
            name: "Product 2",
            price: 20,
            image: "https://via.placeholder.com/150",
            quantity: 2, 
          },
          {
            id: 3,
            name: "Product 3",
            price: 30,
            image: "https://via.placeholder.com/150",
            quantity: 4, 
          },
        ],
      };
    },
    methods: {
      closeModal() {
        this.$emit("close");
      },
      removeItem(item) {
        this.cartItems = this.cartItems.filter((i) => i.id !== item.id);
      },
    },
    computed: {
      cartTotal() {
        return this.cartItems.reduce((total, item) => total + (item.price*item.quantity), 0);
      },
    },
  };
  </script>
  
  <style scoped>
  .modal-card-head, .modal-card-foot {
    justify-content: center;
    align-items: center;
  }
  
  .modal-card-title {
    font-size: 1.5rem;
  }
  
  .cart-item-image {
    width: 100%;
  }
  
  .cart-item-name {
    font-size: 1.2rem;
  }
  
  .cart-item-price {
    font-size: 1.2rem;
    color: #999;
  }
  
  .delete {
    background-color: #ff3860;
    color: white;
    border: none;
    border-radius: 50%;
    padding: 0.5rem;
    width: 2rem;
    height: 2rem;
    font-size: 1.5rem;
  }
  
  .delete:hover {
    background-color: #ff1e43;
  }
  
  .button.is-danger {
    background-color: #ff3860;
    color: white;
    border: none;
  }
  
  .button.is-danger:hover {
    background-color: #ff1e43;
  }
  .cart-total {
  font-size: 1.2rem;
  color: #999;
  margin-right: 1rem;
}
  </style>
  