import axios from "axios";

// Use relative URLs so requests go to the same origin
// that serves the frontend (works for both FastAPI static
// serving in production AND the Vite dev proxy).
const API = axios.create({
  baseURL: "",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 10000,
});

// Predict Customer Churn
export const predictChurn = async (customerData) => {
  try {
    const response = await API.post("/predict", customerData);
    return response.data;
  } catch (error) {
    console.error("Prediction Error:", error);

    if (error.response) {
      throw error.response.data;
    }

    throw {
      detail: "Unable to connect to the FastAPI server.",
    };
  }
};

export default API;
