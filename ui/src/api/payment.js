import axios from 'axios';

export function payCart(type, number, expiration, cvv) {
  addPaymentSystem(type, number, expiration, cvv)
    .then(response => {
      if (response.status === 201) {
        pay();
      }
    });
}

function addPaymentSystem(type, number, expiration, cvv) {
  const url = `${axios.defaults.baseURL}/add_payment_system`;
  const data = {
    type: type,
    number: number,
    expiration_date: expiration,
    cvv: cvv
  }
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  if (access_token_cookie === undefined) {
    alert("You need to be logged in");
  }
  const access_token = access_token_cookie.split('=')[1];
  axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
  return axios.post(url, data)
    .catch(error => {
      if (error.response.status === 400 || error.response.status === 422 || error.response.status === 401){
        alert("You need to be logged in");
      } else {
        alert("Error processing your payment information");
      }
    })
}

function pay() {
  const url = `${axios.defaults.baseURL}/pay`;
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  if (access_token_cookie === undefined) {
    alert("You need to be logged in");
  }
  const access_token = access_token_cookie.split('=')[1];
  axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
  axios.post(url)
    .catch(error => {
      if (error.response.status === 400 || error.response.status === 422 || error.response.status === 401) {
        alert("You need to be logged in");
      } else {
        alert("Error processing your payment information");
      }
    })
    .then(response => {
      if (response.status === 201) {
        alert("Paiement successful");
      }
    });
}
