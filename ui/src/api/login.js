import Cookies from "js-cookie";
import axios from "axios";

export const logIn = async (username, password) => {
  const url = `${axios.defaults.baseURL}/login`;
  try {
    const response = await axios.post(url, {
      username: username,
      password: password,
    });

    let date = new Date();
    const minutes = 180;
    date.setTime(date.getTime() + minutes * 60 * 1000);
    console.log("logIn response data:")
    console.log(response.data);
    Cookies.set("access_token", response.data.access_token, { expires: date });
    console.log("logIn response:")
    console.log(response);
    return response;
  } catch (error) {
    console.log("Error response:");
    console.log(error.response.data);
    return error.response.data;
  }
};



export const getToken = () => {

  const token = Cookies.get("access_token");
  console.log("getToken")
  console.log(Cookies.get("access_token"))
  return token;

}
