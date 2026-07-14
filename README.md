# Customer Churn Prediction 🔮

A full-stack machine learning application that predicts whether a telecom customer is likely to churn. Built with **React** + **FastAPI** + **Scikit-Learn** and deployable via **Docker**.

---

## 🏗️ Architecture

```
┌─────────────────────┐       POST /predict        ┌──────────────────────┐
│   React Frontend    │  ───────────────────────►  │   FastAPI Backend    │
│   (Vite + Tailwind) │  ◄───────────────────────  │   (Uvicorn)          │
│                     │       JSON Response         │                      │
└─────────────────────┘                             │  ┌────────────────┐  │
                                                    │  │ Preprocessor   │  │
                                                    │  │ (pkl)          │  │
                                                    │  ├────────────────┤  │
                                                    │  │ ML Model       │  │
                                                    │  │ (pkl)          │  │
                                                    │  └────────────────┘  │
                                                    └──────────────────────┘
```

## 🚀 Quick Start

### Option 1 — Docker (Recommended)

```bash
docker-compose up --build
```

Open **http://localhost:8000** — both the UI and API are served from a single container.

### Option 2 — Local Development

**Backend:**

```bash
# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**

```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173** — the Vite proxy forwards `/predict` calls to the backend at port 8000.

---

## 📡 API Endpoints

| Method | Endpoint   | Description                    |
|--------|-----------|-------------------------------|
| POST   | `/predict` | Submit customer data for churn prediction |
| GET    | `/health`  | Health check                   |
| GET    | `/docs`    | Swagger UI (interactive API docs) |

### Sample Request

```json
POST /predict
{
  "Gender": "Male",
  "Senior_Citizen": "No",
  "Partner": "Yes",
  "Dependents": "No",
  "Tenure_Months": 12,
  "Phone_Service": "Yes",
  "Multiple_Lines": "No",
  "Internet_Service": "Fiber optic",
  "Online_Security": "No",
  "Online_Backup": "Yes",
  "Device_Protection": "Yes",
  "Tech_Support": "No",
  "Streaming_TV": "Yes",
  "Streaming_Movies": "Yes",
  "Contract": "Month-to-month",
  "Paperless_Billing": "Yes",
  "Payment_Method": "Electronic check",
  "Monthly_Charges": 75.25,
  "Total_Charges": 903.00
}
```

### Sample Response

```json
{
  "prediction": "Churn",
  "prediction_code": 1,
  "probability_no_churn": "32.15%",
  "probability_churn": "67.85%"
}
```

---

## 🛠️ Tech Stack

| Layer     | Technology                         |
|-----------|-----------------------------------|
| Frontend  | React 19, Vite, Tailwind CSS 4    |
| Backend   | FastAPI, Uvicorn, Pydantic        |
| ML        | Scikit-Learn, Pandas, NumPy       |
| Deploy    | Docker, Docker Compose            |

---

## 📂 Project Structure

```
Customer churn predection/
├── app/                    # FastAPI application
│   ├── main.py             # App entry point + CORS + static serving
│   ├── routers.py          # API routes
│   ├── schemas.py          # Pydantic request models
│   └── services.py         # Prediction service layer
├── src/                    # ML source code
│   ├── pipeline/           # Training & prediction pipelines
│   ├── components/         # Data ingestion, transformation, training
│   ├── config.py           # Configuration paths
│   └── utils.py            # Helper utilities
├── artifacts/              # Trained model & preprocessor (.pkl)
├── frontend/               # React application
│   └── src/
│       ├── components/     # Navbar, CustomerForm, PredictionCard, Footer
│       ├── pages/          # Home page
│       └── services/       # Axios API client
├── Dockerfile              # Multi-stage build (Node + Python)
├── docker-compose.yml      # One-command deployment
└── requirements.txt        # Python dependencies
```