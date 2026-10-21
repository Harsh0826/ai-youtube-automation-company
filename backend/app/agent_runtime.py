from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from app.models import AgentDescriptor, AgentStatus, TaskDescriptor, TaskStatus


@dataclass
class AgentRuntime:
    descriptor: AgentDescriptor
    queue: List[str] = field(default_factory=list)
    logs: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def enqueue(self, task_id: str) -> None:
        self.queue.append(task_id)
        self.descriptor.status = AgentStatus.QUEUED

    def start_task(self, task_id: str) -> None:
        self.descriptor.current_task = task_id
        self.descriptor.status = AgentStatus.RUNNING
        self.logs.append(f"Task {task_id} started")

    def complete_task(self, task_id: str, result: Dict[str, Any]) -> None:
        self.descriptor.status = AgentStatus.COMPLETED
        self.descriptor.current_task = ""
        self.logs.append(f"Task {task_id} completed")
        self.metadata["last_result"] = result

    def fail_task(self, task_id: str, reason: str) -> None:
        self.descriptor.status = AgentStatus.FAILED
        self.logs.append(f"Task {task_id} failed: {reason}")
        self.metadata["last_error"] = reason


class RuntimeController:
    def __init__(self, agents: List[AgentDescriptor]) -> None:
        self.agents = {agent.agent_id: AgentRuntime(agent) for agent in agents}
        self.tasks: Dict[str, TaskDescriptor] = {}

    def add_task(
        self,
        workflow_id: str,
        task_type: str,
        title: str,
        description: str = "",
        dependencies: Optional[List[str]] = None,
        agent_id: Optional[str] = None,
    ) -> TaskDescriptor:
        task_id = f"task-{uuid.uuid4().hex[:8]}"
        task = TaskDescriptor(
            task_id=task_id,
            workflow_id=workflow_id,
            task_type=task_type,
            title=title,
            description=description,
            dependencies=dependencies or [],
            agent_id=agent_id,
        )
        self.tasks[task_id] = task
        if agent_id and agent_id in self.agents:
            self.agents[agent_id].enqueue(task_id)
        return task

    def get_agent_status(self, agent_id: str) -> Dict[str, Any]:
        agent = self.agents.get(agent_id)
        if not agent:
            raise KeyError(f"Agent {agent_id} not found")
        return {
            "agent_id": agent.descriptor.agent_id,
            "name": agent.descriptor.name,
            "department": agent.descriptor.department,
            "status": agent.descriptor.status.value,
            "current_task": agent.descriptor.current_task,
            "logs": agent.logs[-5:],
        }

    def run_next_ready_tasks(self) -> List[TaskDescriptor]:
        completed: List[TaskDescriptor] = []
        for task in self.tasks.values():
            if task.status in {TaskStatus.COMPLETED, TaskStatus.FAILED, TaskStatus.CANCELLED}:
                continue
            if task.dependencies:
                if any(self.tasks.get(dep) and self.tasks[dep].status != TaskStatus.COMPLETED for dep in task.dependencies):
                    continue
            if task.agent_id and task.agent_id in self.agents:
                agent_runtime = self.agents[task.agent_id]
                task.status = TaskStatus.RUNNING
                agent_runtime.start_task(task.task_id)
                task.result = {"status": "completed", "agent": task.agent_id}
                task.status = TaskStatus.COMPLETED
                agent_runtime.complete_task(task.task_id, task.result)
                completed.append(task)
        return completed
