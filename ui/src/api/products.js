import axios from 'axios';

export function getProducts() {
  const url = `${axios.defaults.baseURL}/products`;
  return axios.get(url).catch(error => {
    console.log(error);
    alert("Error fetching products");
  });
}
