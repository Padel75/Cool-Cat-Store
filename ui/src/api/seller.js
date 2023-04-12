import axios from 'axios';

export function getSeller(id) {
  const path = `${axios.defaults.baseURL}/seller/${id}`;
  return axios.get(path)
    .catch(error => {
      if (error.response.status === 400) {
        alert("The seller does not exist.");
      } else {
        alert("Error fetching seller infos");
      }
    })
}
