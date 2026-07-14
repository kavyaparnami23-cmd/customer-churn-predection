import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routers import router

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0",
    description="Predict whether a customer will churn."
)

# ── CORS ─────────────────────────────────────────────
# Allow the Vite dev server and common local origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API routes ───────────────────────────────────────
app.include_router(router)


@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}


# ── Serve React frontend in production ───────────────
# When the frontend is built (npm run build), its output
# lands in  frontend/dist/.  Mount it so a single server
# can serve both the API and the UI.
FRONTEND_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "frontend", "dist"
)

if os.path.isdir(FRONTEND_DIR):
    # Serve static assets (JS, CSS, images)
    app.mount(
        "/assets",
        StaticFiles(directory=os.path.join(FRONTEND_DIR, "assets")),
        name="static-assets",
    )

    # Catch-all: serve index.html for any non-API route
    # so React Router works with client-side navigation
    @app.get("/{full_path:path}")
    def serve_spa(full_path: str):
        file_path = os.path.join(FRONTEND_DIR, full_path)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
else:
    @app.get("/")
    def home():
        return {
            "message": "Customer Churn Prediction API is Running",
            "docs": "/docs",
        }