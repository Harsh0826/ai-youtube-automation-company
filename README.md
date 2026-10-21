# AI YouTube Automation Company

A free-first, modular AI media production platform that orchestrates 40 specialized agents to manage research, scripting, asset generation, editing, QA, SEO, publishing, analytics, and growth for YouTube channels.

## Status

Implemented:
- Repository scaffold and project structure
- Free-first architecture and company org model
- 40-agent registry and task orchestration layer
- FastAPI backend with dashboard endpoints
- SQLite-based persistence layer
- Sample end-to-end video pipeline that renders a playable test video with local FFmpeg
- React + Vite dashboard frontend shell
- Security and free-tier design documentation

Partially implemented:
- Real YouTube OAuth and analytics integration
- Full cloud-to-local inference fallback registry
- Advanced avatar/lip-sync pipeline
- Production-grade multi-channel publishing flows

Planned:
- Full n8n/Celery orchestration deployment
- Advanced local image/video generation stack integration
- Complete YouTube Data API automation with approval gates
- Multi-channel social distribution and experiment analytics

## Goals

- Operate from a single dashboard
- Default to $0 cost via local/open-source/free tools
- Keep human approval gates before publishing or paid actions
- Support resumable workflows and graceful recovery

## Quick start

### Prerequisites

- Python 3.11+
- Node.js 20+
- FFmpeg installed and available on PATH
- Optional: Ollama for local LLM usage

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

### Run the sample pipeline

```bash
cd backend
source .venv/bin/activate
python -c "from app.sample_pipeline import create_demo_pipeline; print(create_demo_pipeline())"
```

## Architecture summary

- Backend: FastAPI + SQLAlchemy + SQLite
- Frontend: React + Vite + Tailwind-style CSS
- Queue/orchestration: in-process event-driven task scheduler with persistent task state
- Local AI: Ollama + local TTS + FFmpeg + ComfyUI optional
- Free-first rules: local execution preferred, no silent paid providers

## Security and compliance

- Secrets via .env, not committed
- No publishing without explicit authorization
- No unauthorized voice clones or likenesses
- No fabricated engagement or analytics manipulation
- Approved content and licensing metadata recorded for each asset

## Documentation

- `docs/architecture.md` — system architecture and departments
- `docs/company-org-chart.md` — CEO to department to agent hierarchy
- `docs/project-status.md` — phase tracking and implementation notes
- `docs/troubleshooting.md` — setup and runtime guidance

## Important limitation

This repository implements a real operational framework and a working sample video pipeline using local FFmpeg. It does not claim full autonomous YouTube publishing without user authorization, valid API credentials, and tested access. Actual model, voice, and YouTube integrations should be added only after verifying licensing, rate limits, and hardware constraints.
