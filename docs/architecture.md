# System Architecture

## 1. Platform goals

The project models a free-first AI media company where one person operates a YouTube automation platform from a centralized dashboard. The orchestration layer is manager-first, with event-driven activation of only the agents required for the current task.

## 2. High-level components

- Executive layer: CEO orchestrator, strategy, and portfolio management
- Research layer: trend, competitor, audience, fact-checking
- Content layer: ideation, scoring, calendar, scripting, originality
- Media layer: art direction, image generation, TTS, video generation, music, avatar creation
- Post-production layer: editing, captions, thumbnails, export
- Quality layer: script review, video QA, policy, publishing approval
- SEO and publishing layer: metadata, scheduling, upload preparation
- Marketing and growth layer: engagement, social distribution, campaign planning
- Analytics layer: retention, A/B testing, optimization
- Infrastructure layer: automation, security, cost control, resiliency

## 3. Runtime model

- Event-driven orchestration service
- Persistent task state in SQLite/PostgreSQL
- Producer/consumer queue semantics for jobs
- Dependency graphs and handoff contracts between agents
- Review gates before dispatching resource-heavy tasks

## 4. Data model

```text
project
  ├── channel
  ├── workflow
  ├── task
  ├── asset
  ├── review
  └── analytics
```

Core entities:
- Channel: name, niche, audience, content profile, voice settings
- Workflow: research, scripting, production, export, QA, SEO, publishing
- Task: status, dependencies, retries, owner agent, inputs, outputs
- Asset: file path, license, version, source model/tool
- Review: approval comments, risk flags, human sign-off

## 5. Free-first operating strategy

- Prefer local inference via Ollama or equivalent
- Keep local media assets on disk with cache reuse
- Use FFmpeg-based previews before expensive renders
- Keep quotas visible and enforce pause/fallback behavior
- Use free local models with documented hardware requirements

## 6. Technical stack

Backend:
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite by default, PostgreSQL-ready

Frontend:
- React
- Vite
- TypeScript-ready structure
- Tailwind CSS-inspired styling

Media tooling:
- FFmpeg
- Piper/TTS engine
- Whisper/faster-whisper
- ComfyUI (optional)
- MoviePy

## 7. Production pipeline

1. Research and planning
2. Script and pre-production
3. Asset generation
4. Assembly and editing
5. Verification and release
6. Analytics and improvement

## 8. Human oversight

The system does not auto-publish without approval. It records decisions, approval gates, credentials state, quality checks, and fallback paths.
