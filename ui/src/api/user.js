import axios from 'axios';
import { router } from "@/router";

export function getUser() {
  const path = `${axios.defaults.baseURL}/user_infos`;
  const access_token_cookie = document.cookie.split('; ').find(row => row.startsWith('access_token'));
  if (access_token_cookie === undefined) {
    alert("You need to be logged in to access your page.");
  }
  const access_token = access_token_cookie.split('=')[1];
  axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
  return axios.get(path)
    .catch(error => {
      if (error.response.status === 400) {
        alert("The user does not exist.");
      } else if (error.response.status === 422 || error.response.status === 401) {
        alert("You need to be logged in to access your page.");
      } else {
        alert("Error fetching user infos");
      }
      router.push({ name: "Home" });
    })
}
