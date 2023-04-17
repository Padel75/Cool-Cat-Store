<template>
  <span>{{ invoices }}</span>

</template>

<script>
import { getInvoices } from '@/api/payment';
export default {
  name: 'Invoice',
  data() {
    return {
      invoices: getInvoices().then(response => {
        this.invoices = response.data;
      }),
    };
  },
};
</script>

<style scoped>
.invoice {
  max-width: 960px;
  margin: 0 auto;
  padding: 40px;
  background-color: #fff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.invoice-heading {
  margin-top: 0;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.invoice-details {
  margin-bottom: 20px;
}

.invoice-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.invoice-label {
  font-size: 1.2rem;
  color: #333;
}

.invoice-value {
  font-size: 1.2rem;
  color: #333;
}

.invoice-items {
  margin-bottom: 20px;
}

.invoice-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.invoice-item-name {
  font-size: 1.2rem;
  color: #333;
}

.invoice-item-quantity {
  font-size: 1rem;
  color: #999;
}

.invoice-item-price {
  font-size: 1.2rem;
  color: #333;
}
</style>
