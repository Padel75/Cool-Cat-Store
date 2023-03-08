<template>
  <div class="vendor-page">
    <h1>Vendor Informations</h1>
    <form @submit.prevent="saveVendor" class="vendor-form">
      <div class="form-group">
        <label for="name">Name:  <span v-if="savedVendor.vendorName">{{ savedVendor.vendorName }}</span></label>
        <input type="text" id="name" v-model="vendor.vendorName" >
            </div>
      <div class="form-group">
        <label for="description">Description: <span v-if="savedVendor.description">{{ savedVendor.description }}</span></label>
        <input type="text" id="description" v-model="vendor.description" >
        </div>
      <div class="form-group">
        <label for="phone-number">Phone Number: <span v-if="savedVendor.phoneNumber">{{ savedVendor.phoneNumber }}</span></label>
        <input type="tel" id="phone-number" v-model="vendor.phoneNumber" >
        </div>
      <div class="form-group">
        <label for="email">Email: <span v-if="savedVendor.email">{{ savedVendor.email }}</span></label>
        <input type="email" id="email" v-model="vendor.email" >
        </div>
      <div class="form-group">
        <label for="address">Address: <span v-if="savedVendor.address">{{ savedVendor.address }}</span></label>
        <textarea id="address" v-model="vendor.address" ></textarea>
        </div>
      <button type="submit" class="submit-button">Save Changes</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'VendorForm',
  data() {
    return {
      vendor: {
        vendorName: '',
        description: '',
        phoneNumber: '',
        email: '',
        address: ''
      },
      savedVendor: {
        vendorName: '',
        description: '',
        phoneNumber: '',
        email: '',
        address: ''
      }
    }
  },
  methods: {
    saveVendor() {
      // Save vendor data to backend here
      console.log(this.vendor);
      
      // Store the saved vendor data in the savedVendor object
      this.savedVendor = { ...this.vendor };

      let vendorName = this.savedVendor.vendorName;
      let description = this.savedVendor.description;
      let phoneNumber = this.savedVendor.phoneNumber;
      let email = this.savedVendor.email;
      let address = this.savedVendor.address ;
      
      // Reset form after save to saved
      this.vendor.vendorName = vendorName;
      this.vendor.description = description;
      this.vendor.phoneNumber = phoneNumber;
      this.vendor.email = email;
      this.vendor.address = address ;
    }
  }
}
</script>

<style>
.vendor-page {
  max-width: 800px;
  margin: 0 auto;
}

.vendor-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-group {
  display: flex;
  flex-direction: column;
  text-align: left;
  gap: 5px;
}

label {
  text-align: left;
  font-weight: bold;
}

input, textarea {
  padding: 5px;
  font-size: 16px;
  width: 50%;
  border
: 1px solid #ccc;
}

.submit-button {
  background-color: #0077cc;
  width: 50%;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.submit-button:hover {
  width: 50%;
  background-color: #0060a3;
}
</style>
