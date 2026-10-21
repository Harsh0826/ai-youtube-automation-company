from app.agents_registry import AGENTS
from app.agent_runtime import RuntimeController


DEFAULT_RUNTIME = RuntimeController([agent for agent in AGENTS])
