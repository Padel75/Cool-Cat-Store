<template>
  <seller-form v-on:success-signup="$emit('success-signup')" />
</template>

<script>
import SellerForm from "../views/SellerForm";
export default {
  name: "SignUpSeller",
  components: {
    SellerForm
  }
};
</script>

<style scoped></style>
