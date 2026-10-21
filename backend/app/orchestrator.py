from __future__ import annotations

import uuid
from typing import Any, Dict, List

from app.agents_registry import AGENTS


class CompanyOrchestrator:
    def __init__(self) -> None:
        self.agents = AGENTS

    def get_agents(self) -> List[Dict[str, Any]]:
        return [agent.to_dict() for agent in self.agents]

    def get_workflows(self) -> List[Dict[str, Any]]:
        return [
            {
                "workflow_id": "wf-demo-001",
                "name": "Demo AI Channel Production",
                "channel": "demo-ai-channel",
                "status": "RUNNING",
                "metadata": {
                    "department_count": 10,
                    "agent_count": 40,
                },
            }
        ]

    def get_dashboard_summary(self) -> Dict[str, Any]:
        active = sum(1 for agent in self.agents if agent.status in {"RUNNING", "REVIEW"})
        return {
            "company_name": "AI YouTube Automation Company",
            "active_agents": active,
            "total_agents": len(self.agents),
            "channels": 1,
            "projects": 2,
            "videos_planned": 12,
            "videos_in_production": 2,
            "videos_completed": 7,
            "videos_published": 3,
            "workflow_status": "RUNNING",
            "pending_approvals": 1,
            "estimated_cost": "$0.00",
            "resource_state": {
                "cpu": "available",
                "ram": "available",
                "gpu": "budget-mode",
                "storage": "available",
            },
        }

    def run_sample_workflow(self) -> Dict[str, Any]:
        workflow_id = f"wf-{uuid.uuid4().hex[:8]}"
        return {
            "workflow_id": workflow_id,
            "name": "Demo AI Channel Production",
            "status": "QUEUED",
            "message": "Sample workflow created. Local FFmpeg preview and assembly path is active.",
            "tasks": [
                {"task_id": f"task-{uuid.uuid4().hex[:8]}", "title": "Research", "status": "QUEUED"},
                {"task_id": f"task-{uuid.uuid4().hex[:8]}", "title": "Script and Storyboard", "status": "ASSIGNED"},
                {"task_id": f"task-{uuid.uuid4().hex[:8]}", "title": "Asset Generation", "status": "QUEUED"},
                {"task_id": f"task-{uuid.uuid4().hex[:8]}", "title": "Render Preview", "status": "RUNNING"},
                {"task_id": f"task-{uuid.uuid4().hex[:8]}", "title": "QA and Publish Approval", "status": "REVIEW"},
            ],
        }
