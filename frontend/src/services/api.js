import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export async function predictChurn(formData) {
  const response = await api.post("/predict", formData);
  return response.data;
}

export default api;
