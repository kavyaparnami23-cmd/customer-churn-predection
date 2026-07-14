import { useState } from "react";
import Navbar from "../components/Navbar";
import CustomerForm from "../components/Customerform";
import PredictionCard from "../components/Predictioncard";
import Footer from "../components/footer";
import { predictChurn } from "../services/api";

function Home() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (formData) => {
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      const result = await predictChurn(formData);
      setPrediction(result);
    } catch (err) {
      // api.js already unwraps error.response.data, so err
      // is either { detail: "..." } or { detail: "Unable to connect..." }
      const message =
        err?.detail ||
        err?.message ||
        "Something went wrong. Make sure the backend is running.";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-bg">
      <Navbar />

      <main className="main-content">

        <div className="page-header animate-in">
          <h1 className="page-title">Customer Churn Analysis</h1>
          <p className="page-subtitle">
            Enter customer details below and let our ML model predict whether
            the customer is likely to churn.
          </p>
        </div>

        {error && (
          <div className="error-banner animate-in">
            <span className="error-icon">⚠️</span>
            {error}
          </div>
        )}

        <div className="grid-layout">
          <CustomerForm onSubmit={handleSubmit} loading={loading} />
          <PredictionCard prediction={prediction} loading={loading} />
        </div>

      </main>

      <Footer />
    </div>
  );
}

export default Home;