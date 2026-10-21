from sqlalchemy import JSON, Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

Base = declarative_base()


class AgentRecord(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, default="READY")
    current_task = Column(String, default="")
    metadata = Column(JSON, default=dict)


class TaskRecord(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String, unique=True, index=True)
    workflow_id = Column(String, index=True)
    status = Column(String, default="QUEUED")
    agent_id = Column(String, nullable=True)
    task_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, default="")
    dependencies = Column(JSON, default=list)
    retries = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)
    result = Column(JSON, default=dict)


class WorkflowRecord(Base):
    __tablename__ = "workflows"
    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    channel = Column(String, nullable=False)
    status = Column(String, default="QUEUED")
    metadata = Column(JSON, default=dict)


engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
