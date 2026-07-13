import { useState } from "react";

const INITIAL_STATE = {
  Gender: "Male",
  Senior_Citizen: "No",
  Partner: "No",
  Dependents: "No",
  Tenure_Months: "",
  Phone_Service: "Yes",
  Multiple_Lines: "No",
  Internet_Service: "DSL",
  Online_Security: "No",
  Online_Backup: "No",
  Device_Protection: "No",
  Tech_Support: "No",
  Streaming_TV: "No",
  Streaming_Movies: "No",
  Contract: "Month-to-month",
  Paperless_Billing: "Yes",
  Payment_Method: "Electronic check",
  Monthly_Charges: "",
  Total_Charges: "",
};

function SelectField({ label, name, value, options, onChange }) {
  return (
    <div className="form-group">
      <label className="form-label">{label}</label>
      <select
        className="form-control"
        name={name}
        value={value}
        onChange={onChange}
      >
        {options.map((opt) => (
          <option key={opt} value={opt}>{opt}</option>
        ))}
      </select>
    </div>
  );
}

function NumberField({ label, name, value, onChange, placeholder }) {
  return (
    <div className="form-group">
      <label className="form-label">{label}</label>
      <input
        className="form-control"
        type="number"
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        min="0"
        step="any"
        required
      />
    </div>
  );
}

function CustomerForm({ onSubmit, loading }) {
  const [form, setForm] = useState(INITIAL_STATE);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const payload = {
      ...form,
      Tenure_Months: parseInt(form.Tenure_Months, 10) || 0,
      Monthly_Charges: parseFloat(form.Monthly_Charges) || 0,
      Total_Charges: parseFloat(form.Total_Charges) || 0,
    };
    onSubmit(payload);
  };

  return (
    <div className="glass-card animate-in delay-1">
      <div className="card-header">
        <div className="card-icon card-icon-form">👤</div>
        <div>
          <h2 className="card-title">Customer Information</h2>
          <p className="card-desc">Enter customer details to predict churn</p>
        </div>
      </div>

      <div className="card-body">
        <form onSubmit={handleSubmit}>

          {/* Demographics */}
          <div className="form-section">
            <div className="section-label">
              <span className="section-label-icon">🏷️</span> Demographics
            </div>
            <div className="form-grid">
              <SelectField label="Gender" name="Gender" value={form.Gender} options={["Male", "Female"]} onChange={handleChange} />
              <SelectField label="Senior Citizen" name="Senior_Citizen" value={form.Senior_Citizen} options={["Yes", "No"]} onChange={handleChange} />
              <SelectField label="Partner" name="Partner" value={form.Partner} options={["Yes", "No"]} onChange={handleChange} />
              <SelectField label="Dependents" name="Dependents" value={form.Dependents} options={["Yes", "No"]} onChange={handleChange} />
            </div>
          </div>

          {/* Services */}
          <div className="form-section">
            <div className="section-label">
              <span className="section-label-icon">📡</span> Services
            </div>
            <div className="form-grid">
              <SelectField label="Phone Service" name="Phone_Service" value={form.Phone_Service} options={["Yes", "No"]} onChange={handleChange} />
              <SelectField label="Multiple Lines" name="Multiple_Lines" value={form.Multiple_Lines} options={["Yes", "No", "No phone service"]} onChange={handleChange} />
              <SelectField label="Internet Service" name="Internet_Service" value={form.Internet_Service} options={["DSL", "Fiber optic", "No"]} onChange={handleChange} />
              <SelectField label="Online Security" name="Online_Security" value={form.Online_Security} options={["Yes", "No", "No internet service"]} onChange={handleChange} />
              <SelectField label="Online Backup" name="Online_Backup" value={form.Online_Backup} options={["Yes", "No", "No internet service"]} onChange={handleChange} />
              <SelectField label="Device Protection" name="Device_Protection" value={form.Device_Protection} options={["Yes", "No", "No internet service"]} onChange={handleChange} />
              <SelectField label="Tech Support" name="Tech_Support" value={form.Tech_Support} options={["Yes", "No", "No internet service"]} onChange={handleChange} />
              <SelectField label="Streaming TV" name="Streaming_TV" value={form.Streaming_TV} options={["Yes", "No", "No internet service"]} onChange={handleChange} />
              <SelectField label="Streaming Movies" name="Streaming_Movies" value={form.Streaming_Movies} options={["Yes", "No", "No internet service"]} onChange={handleChange} />
            </div>
          </div>

          {/* Account & Billing */}
          <div className="form-section">
            <div className="section-label">
              <span className="section-label-icon">💳</span> Account & Billing
            </div>
            <div className="form-grid">
              <NumberField label="Tenure (Months)" name="Tenure_Months" value={form.Tenure_Months} onChange={handleChange} placeholder="e.g. 12" />
              <SelectField label="Contract" name="Contract" value={form.Contract} options={["Month-to-month", "One year", "Two year"]} onChange={handleChange} />
              <SelectField label="Paperless Billing" name="Paperless_Billing" value={form.Paperless_Billing} options={["Yes", "No"]} onChange={handleChange} />
              <SelectField label="Payment Method" name="Payment_Method" value={form.Payment_Method} options={["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]} onChange={handleChange} />
              <NumberField label="Monthly Charges ($)" name="Monthly_Charges" value={form.Monthly_Charges} onChange={handleChange} placeholder="e.g. 75.50" />
              <NumberField label="Total Charges ($)" name="Total_Charges" value={form.Total_Charges} onChange={handleChange} placeholder="e.g. 903.00" />
            </div>
          </div>

          <button type="submit" className="btn-predict" disabled={loading}>
            {loading ? (
              <><span className="spinner"></span>Analyzing...</>
            ) : (
              "🔍  Predict Churn"
            )}
          </button>

        </form>
      </div>
    </div>
  );
}

export default CustomerForm;