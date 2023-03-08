<template>
  <SignInForm/>
  <CustomerForm/>
  <ProductFormPage/>
  <VendorPage/>
</template>

<script>
import SignInForm from './components/SignInPage.vue'
import CustomerForm from './components/CustomerPage.vue'
import ProductFormPage from './components/ProductFormPage.vue'
import VendorPage from './components/VendorPage.vue'

export default {
  name: 'App',
  components: {
    SignInForm,
    CustomerForm,
    ProductFormPage,
    VendorPage

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
