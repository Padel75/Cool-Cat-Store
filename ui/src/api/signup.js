import axios from "axios";


export const signUpSeller = async (username, password, name, description,address , phone_number, email) => {
  const url = `${axios.defaults.baseURL}/signup/seller`;
  try {
    const response = await axios.post(url, {
      username: username,
      password: password,
      name: name,
      description: description,
      address: address,
      phone_number: phone_number,
      email: email
    });
    return response;
  } catch (error) {
    console.log("Error response:");
    console.log(error.response.data);
    return error.response.data;
  }
};

export const signUpCustomer = async (username, password, first_name, last_name, address , phone_number, email) => {
  const url = `${axios.defaults.baseURL}/signup/customer`;
    try {
      const response = await axios.post(url, {
          username: username,
          password: password,
          first_name: first_name,
          last_name: last_name,
          address: address,
          phone_number: phone_number,
          email: email,
        });
        return response;
  } catch (error) {
    console.log("Error response:");
    console.log(error.response.data);
    return error.response.data;
  }
};
