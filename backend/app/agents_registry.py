from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AgentDefinition:
    agent_id: str
    name: str
    department: str
    role: str
    status: str = "READY"
    current_task: str = ""
    tools: List[str] = field(default_factory=list)
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    success_criteria: str = "Task completed with required review and logs"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "department": self.department,
            "role": self.role,
            "status": self.status,
            "current_task": self.current_task,
            "tools": self.tools,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "success_criteria": self.success_criteria,
        }


AGENTS: List[AgentDefinition] = [
    AgentDefinition("CEO-01", "CEO Orchestrator", "Executive Management and Strategy", "Manages overall platform and production planning", tools=["scheduler", "project-plan", "approval-gate"], inputs=["company goals", "resource state"], outputs=["strategy plan", "task assignments"], success_criteria="Production plan and approvals are issued"),
    AgentDefinition("STR-02", "YouTube Business Strategist", "Executive Management and Strategy", "Defines channel positioning and monetization strategy", tools=["market-analysis", "goal-tracker"], inputs=["channel profile", "business goals"], outputs=["growth plan", "targets"], success_criteria="Targets and channel strategy are documented"),
    AgentDefinition("STR-03", "Niche Research Analyst", "Executive Management and Strategy", "Analyzes niche opportunity and sustainable demand", tools=["niche-scorer", "research-db"], inputs=["niche options"], outputs=["niche report"], success_criteria="Ranked niche recommendation is created"),
    AgentDefinition("STR-04", "Content Portfolio Manager", "Executive Management and Strategy", "Allocates content and maintains calendar balance", tools=["portfolio-planner", "calendar"], inputs=["content ideas", "capacity"], outputs=["portfolio plan"], success_criteria="Publishing mix is balanced and non-redundant"),
    AgentDefinition("RES-05", "Trend Discovery Agent", "Research and Intelligence", "Discovers trend momentum from public sources", tools=["trend-api", "search"], inputs=["topic candidate"], outputs=["trend brief"], success_criteria="Signals are identified and sourced"),
    AgentDefinition("RES-06", "Competitor Analysis Agent", "Research and Intelligence", "Studies public competitor content formats and gaps", tools=["web-scrape", "analysis"], inputs=["competitor channels"], outputs=["competitor brief"], success_criteria="Differentiation opportunities are noted"),
    AgentDefinition("RES-07", "Audience Research Agent", "Research and Intelligence", "Builds audience personas and topical preferences", tools=["persona-analysis", "comment-review"], inputs=["audience samples"], outputs=["audience profile"], success_criteria="Audience needs and tone are profiled"),
    AgentDefinition("RES-08", "Fact-Checking and Source Verification Agent", "Research and Intelligence", "Verifies claims and sources", tools=["source-checker"], inputs=["draft claims"], outputs=["verification report"], success_criteria="Claims are checked and risky items flagged"),
    AgentDefinition("DEV-09", "Content Ideation Agent", "Content Development", "Generates diverse video concepts and recurring formats", tools=["idea-generator", "backlog"], inputs=["topic pool"], outputs=["concept list"], success_criteria="Multiple original concepts are generated"),
    AgentDefinition("DEV-10", "Topic Scoring Agent", "Content Development", "Scores topics by demand, feasible production, and value", tools=["scoring-model"], inputs=["candidate topics"], outputs=["scorecard"], success_criteria="Topics are ranked with rationale"),
    AgentDefinition("DEV-11", "Content Calendar Manager", "Content Development", "Builds editorial calendar and priority plan", tools=["calendar", "resource-planner"], inputs=["approved topics"], outputs=["production calendar"], success_criteria="Publishing schedule is aligned to capacity"),
    AgentDefinition("DEV-12", "Scriptwriting Agent", "Content Development", "Creates scripts, dialogue, and narration structure", tools=["llm", "story-template"], inputs=["idea brief"], outputs=["script draft"], success_criteria="Narrative structure and timing are complete"),
    AgentDefinition("DEV-13", "Storytelling and Retention Agent", "Content Development", "Improves hooks, pacing, and pattern interrupts", tools=["retention-analysis"], inputs=["script draft"], outputs=["retention edit"], success_criteria="Opening hook and pacing are improved"),
    AgentDefinition("DEV-14", "Originality and Copyright Review Agent", "Content Development", "Flags similarity and potential licensing issues", tools=["copyright-check", "originality-review"], inputs=["script and assets"], outputs=["risk report"], success_criteria="Risks are documented before production"),
    AgentDefinition("MED-15", "Visual Art Director", "AI Media Production", "Creates visual identity and composition guidelines", tools=["moodboard", "art-guidelines"], inputs=["video brief"], outputs=["visual spec"], success_criteria="Visual direction is consistent and documented"),
    AgentDefinition("MED-16", "Image Generation Agent", "AI Media Production", "Generates scenes, props, and supporting visuals", tools=["comfyui", "image-model"], inputs=["scene prompts"], outputs=["image assets"], success_criteria="Required visual assets are generated or reused"),
    AgentDefinition("MED-17", "Character and Avatar Creation Agent", "AI Media Production", "Designs original characters and avatar references", tools=["avatar-designer", "reference-library"], inputs=["character brief"], outputs=["character sheet"], success_criteria="Characters remain consistent across scenes"),
    AgentDefinition("MED-18", "AI Voice Production Agent", "AI Media Production", "Generates narration and dialogue with TTS tools", tools=["piper", "tts-engine"], inputs=["script audio lines"], outputs=["voice audio"], success_criteria="Voice and pacing are acceptable and consistent"),
    AgentDefinition("MED-19", "Lip-Sync Agent", "AI Media Production", "Synchronizes dialogue with mouth movement when supported", tools=["lip-sync", "animation-fallback"], inputs=["voice track", "character references"], outputs=["synced animation"], success_criteria="Audio and animation align within tolerance"),
    AgentDefinition("MED-20", "AI Video Generation Agent", "AI Media Production", "Generates clips from scenes and prompts", tools=["local-video", "video-model"], inputs=["scene plan"], outputs=["video clips"], success_criteria="Clip generation completes or fallback is selected"),
    AgentDefinition("MED-21", "Music and Sound Design Agent", "AI Media Production", "Creates or selects licensed sound treatment", tools=["audio-library", "sfx-generator"], inputs=["video pace", "scene mood"], outputs=["audio mix"], success_criteria="Music and sound do not overpower dialogue"),
    AgentDefinition("EDT-22", "Video Editing Agent", "Editing and Post-Production", "Assembles clips and transitions in edit sequence", tools=["ffmpeg", "editing-template"], inputs=["media assets"], outputs=["edit timeline"], success_criteria="Timeline is assembled and previewable"),
    AgentDefinition("EDT-23", "Subtitle and Caption Agent", "Editing and Post-Production", "Generates timed captions and subtitle files", tools=["whisper", "subtitle-generator"], inputs=["final audio/video"], outputs=["captions"], success_criteria="Captions are synced and readable"),
    AgentDefinition("EDT-24", "Thumbnail and Graphic Design Agent", "Editing and Post-Production", "Creates platform-appropriate thumbnails", tools=["design-template", "image-editor"], inputs=["video concept"], outputs=["thumbnail variants"], success_criteria="Thumbnail is clear and non-deceptive"),
    AgentDefinition("EDT-25", "Format and Export Agent", "Editing and Post-Production", "Exports final aspect ratio and codec deliverables", tools=["ffmpeg", "export-profile"], inputs=["edited master"], outputs=["final export"], success_criteria="Output passes resolution and integrity checks"),
    AgentDefinition("QA-26", "Script Quality Reviewer", "Quality Assurance and Compliance", "Reviews clarity, pacing, and factual consistency", tools=["review-checklist"], inputs=["script draft"], outputs=["script QA"], success_criteria="Script passes editorial review or is revised"),
    AgentDefinition("QA-27", "Video Quality Assurance Agent", "Quality Assurance and Compliance", "Checks visual glitches, audio integrity, and subtitle quality", tools=["frame-checker", "audio-validator"], inputs=["exported video"], outputs=["quality report"], success_criteria="Video passes technical checks"),
    AgentDefinition("QA-28", "YouTube Policy and Safety Agent", "Quality Assurance and Compliance", "Flags policy-sensitive or risky material", tools=["policy-rules", "safety-check"], inputs=["video and metadata"], outputs=["safety review"], success_criteria="Reviewed content is documented and approved or flagged"),
    AgentDefinition("QA-29", "Final Release Manager", "Quality Assurance and Compliance", "Collects approvals and authorizes publication", tools=["approval-gate", "release-checklist"], inputs=["QA reports"], outputs=["release decision"], success_criteria="Final approval or block is logged"),
    AgentDefinition("SEO-30", "YouTube SEO Agent", "SEO and Publishing", "Researches keywords and metadata improvements", tools=["keyword-research", "metadata-optimizer"], inputs=["topic and script"], outputs=["SEO metadata"], success_criteria="Titles and metadata are relevant and compliant"),
    AgentDefinition("SEO-31", "Metadata and Localization Agent", "SEO and Publishing", "Formats descriptions, captions, and multilingual metadata", tools=["localization", "translation"], inputs=["final script and assets"], outputs=["localized package"], success_criteria="Metadata and captions are complete and consistent"),
    AgentDefinition("SEO-32", "Upload and Scheduling Agent", "SEO and Publishing", "Prepares upload and scheduling tasks", tools=["youtube-data-api", "scheduler"], inputs=["final asset package"], outputs=["scheduled upload"], success_criteria="Upload is prepared and is ready only after approval"),
    AgentDefinition("MKT-33", "Audience Engagement Agent", "Marketing and Growth", "Reviews audience comments and suggests responses", tools=["engagement-monitor"], inputs=["public comments and reactions"], outputs=["engagement notes"], success_criteria="Issues are triaged and risky interactions flagged"),
    AgentDefinition("MKT-34", "Social Media Distribution Agent", "Marketing and Growth", "Repurposes content for supported platforms", tools=["social-publisher"], inputs=["approved video"], outputs=["promotional assets"], success_criteria="Platform-specific teasers are prepared within rate limits"),
    AgentDefinition("MKT-35", "Community and Campaign Manager", "Marketing and Growth", "Plans launch strategy and recurring campaigns", tools=["campaign-planner"], inputs=["channel objectives"], outputs=["campaign calendar"], success_criteria="Launch plan is documented and measurable"),
    AgentDefinition("ANA-36", "Performance Analytics Agent", "Analytics and Optimization", "Collects available views and retention metrics", tools=["analytics-api"], inputs=["published content"], outputs=["performance report"], success_criteria="Metrics are gathered and separated from estimates"),
    AgentDefinition("ANA-37", "A/B Testing and Experimentation Agent", "Analytics and Optimization", "Runs controlled experiments on titles and thumbnails", tools=["experimentation"], inputs=["videos and metadata"], outputs=["experiment plan"], success_criteria="Test conditions are defined and results are tracked"),
    AgentDefinition("ANA-38", "Recommendation and Optimization Agent", "Analytics and Optimization", "Suggests patterns and future content changes", tools=["optimization-engine"], inputs=["performance data"], outputs=["optimization recommendations"], success_criteria="Suggestions are based on observed data and guardrails"),
    AgentDefinition("INF-39", "Automation and Integration Engineer", "Infrastructure and Reliability", "Maintains workflow orchestration and service fallbacks", tools=["queue-engine", "retry-layer"], inputs=["task execution events"], outputs=["recovery plan"], success_criteria="Tasks resume safely after failures"),
    AgentDefinition("INF-40", "Infrastructure, Security and Cost Controller", "Infrastructure and Reliability", "Protects secrets, budgets, and system integrity", tools=["cost-monitor", "audit-logger"], inputs=["system state"], outputs=["safety and cost report"], success_criteria="No unauthorized spend or secret leak occurs"),
]
