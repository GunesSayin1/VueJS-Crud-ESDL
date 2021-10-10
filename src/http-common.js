import axios from "axios";

export default axios.create({
  headers: {
    baseURL: "http://0.0.0.0:5000",
    "Content-type": "application/json",
  },
});
