<template>
  <customer-form v-on:success-signup="$emit('success-signup')" />
</template>

<script>
import CustomerForm from "../views/CustomerForm.vue";
export default {
  name: "SignUpCustomer",
  components: {
    CustomerForm
  }
};
</script>

<style scoped></style>
