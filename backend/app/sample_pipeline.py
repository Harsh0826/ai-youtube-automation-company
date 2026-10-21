import json
import os
import subprocess
from pathlib import Path


class DemoVideoPipeline:
    def __init__(self, output_dir: str = "/tmp/ai_youtube_demo") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def create_demo_video(self, video_name: str = "demo_video.mp4") -> dict:
        output_path = self.output_dir / video_name
        ffmpeg_path = "ffmpeg"
        if not self._has_ffmpeg():
            raise RuntimeError("FFmpeg is required but was not found on PATH.")

        cmd = [
            ffmpeg_path,
            "-y",
            "-f",
            "lavfi",
            "-i",
            "color=c=0x1d4ed8:s=1280x720:d=6",
            "-vf",
            "drawtext=text='AI YouTube Automation Company':fontcolor=white:fontsize=54:x=(w-text_w)/2:y=(h-text_h)/2,drawbox=x=50:y=50:w=1180:h=80:color=black@0.25:t=fill",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            str(output_path),
        ]
        subprocess.run(cmd, check=True)
        return {
            "status": "completed",
            "path": str(output_path),
            "duration_seconds": 6,
            "aspect_ratio": "16:9",
            "format": "mp4",
        }

    def _has_ffmpeg(self) -> bool:
        return subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True).returncode == 0


def create_demo_pipeline() -> dict:
    pipeline = DemoVideoPipeline()
    result = pipeline.create_demo_video()
    return {
        "workflow": "demo-ai-video-pipeline",
        "status": "completed",
        "result": result,
        "free_mode": True,
        "notes": [
            "Generated using local FFmpeg to avoid paid rendering services.",
            "Preview output is suitable for QA and demo review.",
        ],
    }
