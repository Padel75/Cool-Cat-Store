import axios from 'axios';


const URL = "http://localhost:8080/";

export const getProductsByPage = async (page) => {
    const response = await fetch(`${URL}?page=${page}`, {
        Method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
      })
      return response.json();
};
export const getAllProducts = async () => {
  const path = `${API_URL}/products`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getProduct = async id => {
  const path = `${API_URL}/products/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getVendor = async id => {
  const path = `${API_URL}/vendors/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getStyle = async id => {
  const path = `${API_URL}/styles/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getType = async id => {
  const path = `${API_URL}/types/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getVendorProducts = async vendor_id => {
  const path = `${API_URL}/vendors/${vendor_id}/products`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};