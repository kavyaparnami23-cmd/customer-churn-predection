function PredictionCard({ prediction, loading }) {

  const CIRCUMFERENCE = 2 * Math.PI * 70;

  if (!prediction && !loading) {
    return (
      <div className="glass-card animate-in delay-2">
        <div className="card-header">
          <div className="card-icon card-icon-result">📊</div>
          <div>
            <h2 className="card-title">Prediction Result</h2>
            <p className="card-desc">Results will appear here</p>
          </div>
        </div>
        <div className="card-body">
          <div className="prediction-empty">
            <div className="empty-icon">🔮</div>
            <p className="empty-title">No Prediction Yet</p>
            <p className="empty-desc">
              Fill in the customer details and click Predict to see the churn analysis.
            </p>
          </div>
        </div>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="glass-card animate-in delay-2">
        <div className="card-header">
          <div className="card-icon card-icon-result">📊</div>
          <div>
            <h2 className="card-title">Prediction Result</h2>
            <p className="card-desc">Analyzing customer data...</p>
          </div>
        </div>
        <div className="card-body">
          <div className="prediction-empty">
            <div className="spinner" style={{ width: 40, height: 40, borderWidth: 4 }}></div>
            <p className="empty-title" style={{ marginTop: 24 }}>Running ML Model...</p>
            <p className="empty-desc">Processing through the prediction pipeline</p>
          </div>
        </div>
      </div>
    );
  }

  const isChurn = prediction.prediction === "Churn";
  const churnProbRaw = parseFloat(prediction.probability_churn);
  const noChurnProbRaw = parseFloat(prediction.probability_no_churn);
  const displayProb = isChurn ? churnProbRaw : noChurnProbRaw;
  const offset = CIRCUMFERENCE - (displayProb / 100) * CIRCUMFERENCE;

  return (
    <div className="glass-card animate-in delay-2">
      <div className="card-header">
        <div className="card-icon card-icon-result">📊</div>
        <div>
          <h2 className="card-title">Prediction Result</h2>
          <p className="card-desc">ML model analysis complete</p>
        </div>
      </div>

      <div className="card-body" style={{ textAlign: "center" }}>

        {/* Gauge */}
        <div className="gauge-container">
          <svg className="gauge-svg" viewBox="0 0 160 160">
            <defs>
              <linearGradient id="gradient-safe" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stopColor="#34d399" />
                <stop offset="100%" stopColor="#6ee7b7" />
              </linearGradient>
              <linearGradient id="gradient-risk" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stopColor="#f87171" />
                <stop offset="100%" stopColor="#fbbf24" />
              </linearGradient>
            </defs>
            <circle className="gauge-track" cx="80" cy="80" r="70" />
            <circle
              className={`gauge-fill ${isChurn ? "gauge-fill-risk" : "gauge-fill-safe"}`}
              cx="80"
              cy="80"
              r="70"
              strokeDasharray={CIRCUMFERENCE}
              strokeDashoffset={offset}
            />
          </svg>

          <div className="gauge-center-text">
            <div className={`gauge-percent ${isChurn ? "gauge-percent-risk" : "gauge-percent-safe"}`}>
              {displayProb.toFixed(1)}%
            </div>
            <div className="gauge-label">
              {isChurn ? "Churn Risk" : "Retention Confidence"}
            </div>
          </div>
        </div>

        {/* Verdict */}
        <div className={`verdict-badge ${isChurn ? "verdict-risk" : "verdict-safe"}`}>
          <span style={{ fontSize: 20 }}>{isChurn ? "⚠️" : "✅"}</span>
          {isChurn ? "High Churn Risk" : "Customer Likely to Stay"}
        </div>

        {/* Probability Breakdown */}
        <div className="prob-section">
          <div className="prob-row">
            <span className="prob-label">Retention Probability</span>
            <span className="prob-value">{prediction.probability_no_churn}</span>
          </div>
          <div className="prob-bar-track">
            <div
              className="prob-bar-fill prob-bar-safe"
              style={{ width: `${noChurnProbRaw}%` }}
            ></div>
          </div>

          <div className="prob-row">
            <span className="prob-label">Churn Probability</span>
            <span className="prob-value">{prediction.probability_churn}</span>
          </div>
          <div className="prob-bar-track">
            <div
              className="prob-bar-fill prob-bar-risk"
              style={{ width: `${churnProbRaw}%` }}
            ></div>
          </div>
        </div>

      </div>
    </div>
  );
}

export default PredictionCard;
