import axios from 'axios';
import { router } from "@/router";

export function getCart() {
  const url = `${axios.defaults.baseURL}/cart`;
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  if (access_token_cookie === undefined) {
    alert("You need to be logged in");
  }
  const access_token = access_token_cookie.split('=')[1];
  axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
  return axios.get(url)
    .catch(error => {
    if (error.response.status === 400){
    alert("You need to be logged in");
    }
    else {
      alert("Error fetching cart");
    }
  })
}

export function addToCart(productId, quantity) {
  const url = `${axios.defaults.baseURL}/add_to_cart/${productId}`;
  console.log(url)
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  if (access_token_cookie === undefined) {
    alert("You need to be logged in");
  }
  const access_token = access_token_cookie.split('=')[1];
  axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
  const data = {
    quantity: quantity
  }
  axios.post(url, data)
    .catch(error => {
      if (error.response.status === 400) {
        alert("You need to be logged in");
      } else {
        alert("Error adding to cart");
      }
    })
    .then(response => {
      if (response.status === 201) {
        router.go(0);
      }
    });
}

export function removeFromCart(productId) {
  console.log("removeFromCart")
  addToCart(productId, 0);
}
