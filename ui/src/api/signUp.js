import axios from "axios";

export function signUpCustomer(username, password, firstName, lastName, phoneNumber, email, address){
  const url = `${axios.defaults.baseURL}/signup/customer`;
  const newCustomer = {
    username: username,
    password: password,
    first_name: firstName,
    last_name: lastName,
    address: address,
    phone_number: phoneNumber,
    email: email
  };
  axios.post(url, newCustomer)
    .then(response => {
      if (response.status === 200) {
        this.$router.push({ name: 'CustomerPage', params: { id: response.data.id } }); // on retourne quoi ici, l'ID ou les params du client?
      }
    })
    .catch(error => {
        alert("Something went wrong");
      });
}

export function signUpSeller(name, description, address, email, phoneNumber) {
  const url = `${axios.defaults.baseURL}/signup/seller`;
  const newSeller = {
    username: "Joe123", //à ajouter
    password: "1234567889",
    name: name,
    description: description,
    address: address,
    email: email,
    phone_number: phoneNumber
  };
  console.log(newSeller);
  axios.post(url, newSeller)
    .then(response => {
      if (response.status === 201) {
        this.$router.push({ name: 'SellerPage', params: { id: response.data.id } });
      }
    })
    .catch(error => {
        alert("Something went wrong");
      });
}

