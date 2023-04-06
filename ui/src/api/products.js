import axios from 'axios';
import { router } from "@/router";

export function getProducts() {
  console.log("getProducts() called");
  const url = `${axios.defaults.baseURL}/products`;
  return axios.get(url).catch(error => {
    console.log(error);
    alert("Error fetching products");
  });
}
