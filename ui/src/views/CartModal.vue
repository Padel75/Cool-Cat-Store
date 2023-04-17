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
            <li v-for="item in cartItems" :key="item.product.id">
              <div class="columns is-vcentered">
                <div class="column is-3">
                  <img :src="item.product.image" :alt="item.product.name" class="cart-item-image">
                </div>
                <div class="column is-6">
                  <p class="cart-item-name">{{ item.product.name }}</p>
                  <p class="cart-item-price">$ {{ item.product.price }}</p>
                  <p class="cart-item-quantity">qty: {{ item.quantity }}</p>
                </div>
                <div class="column is-3">
                  <button class="delete is-large" aria-label="remove item" @click="removeItem(item.product.id)"></button>
                </div>
              </div>
            </li>
          </ul>
          <p class="cart-total-price">Total: {{ this.totalCost }} $ </p>
        </section>
        <footer class="modal-card-foot">
          <router-link class="form-button"
             v-bind:class="{ 'inactive-button': this.totalCost === 0 }"
             to="/payment"
             @click.native="$emit('close')">Checkout</router-link>
        </footer>
      </div>
    </div>
  </template>

  <script>
  import { getCart } from "@/api/cart";
  import { removeFromCart } from "@/api/cart";
  import { useUserStore} from "@/stores/user";
  import { useRouter } from "vue-router";
const router = useRouter();


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
        cartItems: [],
        totalCost: 0,
      };
    },
    mounted() {
      this.fetchCart();
    },
    methods: {
      fetchCart() {
        const userStore = useUserStore();
        if (userStore.isCustomer){
          getCart().then((response) => {
            this.cartItems = response.data.cart;
            this.totalCost = response.data.total_cost;
          });
        }
      },
      closeModal() {
        this.$emit("close");
      },
      removeItem(productId) {
        removeFromCart(productId);
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
    width: 200px;
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
  .inactive-button {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}
  </style>
