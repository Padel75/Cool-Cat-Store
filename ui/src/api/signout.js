import axios from "axios";
import Cookies from "js-cookie";
import {router} from "@/router";

export const signOut = async () => {

  const url = `${axios.defaults.baseURL}/signout`;
    const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
    if (access_token_cookie === undefined) {
      alert("You need to be logged in before signing out");
    }
    const access_token = access_token_cookie.split('=')[1];
    axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
    return axios.delete(url)
      .catch(error => {
       if (error.response.status === 401) {
        alert("You need to be logged in to sign out");
      }
      else {
        alert("Error signing out");
      }
    })
      .then(response => {
        if (response.status === 200) {
          Cookies.remove("access_token" , { path: '/' }); //fonctionne pas.......
          router.push({
            name: "Login",
            params: {
              returnUrl: `${axios.defaults.baseURL}/login`,
            },
          });
        }
      })
}
