import axios from 'axios';

export function getProducts() {
  const url = `${axios.defaults.baseURL}/products`;
  return axios.get(url).catch(error => {
    console.log(error);
    alert("Error fetching products");
  });
}

export function getProduct(id) {
  const url = `${axios.defaults.baseURL}/products/${id}`;
  return axios.get(url).catch(error => {
    console.log(error);
    alert("Error fetching product");
  });
}

export function getSellerProducts(id) {
  const path = `${axios.defaults.baseURL}/seller/${id}/products`;
  return axios.get(path)
    .catch(error => {
      if (error.response.status === 400) {
        alert("The seller does not exist.");
      } else {
        alert("Error fetching product");
      }
    })
}
