from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import init_db
from app.orchestrator import CompanyOrchestrator

app = FastAPI(title=settings.app_name, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize default stores
init_db()
company = CompanyOrchestrator()


@app.get("/api/health")
def health() -> dict:
    return {
        "status": "ok",
        "app": settings.app_name,
        "free_mode": settings.allow_paid_services is False,
        "database": settings.database_url,
    }


@app.get("/api/dashboard")
def dashboard_summary() -> dict:
    return company.get_dashboard_summary()


@app.get("/api/agents")
def agents() -> dict:
    return {"agents": company.get_agents()}


@app.get("/api/workflows")
def workflows() -> dict:
    return {"workflows": company.get_workflows()}


@app.post("/api/workflows/sample")
def run_sample_workflow() -> dict:
    return company.run_sample_workflow()


@app.get("/")
def index() -> dict:
    return {"message": "AI YouTube Automation Company backend"}
