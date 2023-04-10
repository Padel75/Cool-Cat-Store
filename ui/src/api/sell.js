import axios from 'axios';
import { router } from "@/router";

export function sellProduct(product) {
  const url = `${axios.defaults.baseURL}/sell`;
  const data = {
    name: product.name,
    size: product.size,
    image_src: product.image,
    price: product.price,
    category: product.category
  };
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  if (access_token_cookie === undefined) {
    alert("You need to be logged in as a seller to sell a product");
  }
  const access_token = access_token_cookie.split('=')[1];
  axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
  return axios.post(url, data)
    .catch(error => {
    if (error.response.status === 400){
      alert("You are logged in as a buyer. You need to be logged in as a seller to sell a product");
    }
    else if (error.response.status === 422 || error.response.status === 401) {
      alert("You need to be logged in as a seller to sell a product");
    }
    else {
      alert("Error selling product");
    }
  })
    .then(response => {
      if (response.status === 201) {
        router.push({ name: "Product", params: { id: response.data.product_id },
         props: {
          product:  data
      } });
      }
    })
}
