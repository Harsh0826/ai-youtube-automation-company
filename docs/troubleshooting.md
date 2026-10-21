# Troubleshooting Guide

## Backend won't start

- Ensure Python 3.11+ is installed
- Create a virtual environment and install dependencies
- Confirm `ffmpeg` is in PATH
- Check `.env` values for local settings

## Frontend won't load

- Ensure Node.js 20+ is installed
- Run `npm install`
- Confirm the backend is running on port 8000

## FFmpeg fails

- Install FFmpeg for your OS
- Verify with `ffmpeg -version`
- Ensure output directories are writable

## Local model tools missing

- Ollama may be installed locally or omitted
- The platform falls back to local FFmpeg-based demo generation when LLM models are unavailable
- Full AI generation must be validated against actual hardware and OS support

## Publishing blocked

- Publishing is intentionally gated behind human approval
- The platform will not publish without account authorization and config
