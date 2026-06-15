#!/usr/bin/env bash
# Live-demo launcher: runs the assistant locally on the recommended 3B-Q8 config
# and exposes it on a temporary public URL via a Cloudflare quick tunnel.
#
# This keeps the thesis claim intact: the model still runs FULLY LOCAL (Ollama on
# this machine). Cloudflare only forwards HTTP to localhost:8501 — no data leaves
# to a third-party LLM. The public https://*.trycloudflare.com URL lives only while
# this script runs, needs no Cloudflare account, and dies on Ctrl-C.
#
# Prereqs:
#   - Ollama installed + running   (https://ollama.com)
#   - cloudflared installed        (brew install cloudflared)
#   - uv installed                 (project already uses it)
#
# Usage:
#   ./scripts/demo.sh                         # 3B-Q8 (recommended config)
#   LICENTA_MODEL=qwen2.5:3b-instruct-q4_K_M ./scripts/demo.sh   # override model
#   PORT=8600 ./scripts/demo.sh               # override port
set -euo pipefail
cd "$(dirname "$0")/.."

export LICENTA_MODEL="${LICENTA_MODEL:-qwen2.5:3b-instruct-q8_0}"
PORT="${PORT:-8501}"
echo "==> Model: $LICENTA_MODEL  |  port: $PORT"

# 1. Make sure Ollama is up (start it in the background if not).
if ! curl -sf http://localhost:11434/api/version >/dev/null 2>&1; then
  echo "==> Starting 'ollama serve' in the background…"
  ollama serve >/tmp/licenta_ollama.log 2>&1 &
  for _ in $(seq 1 30); do
    curl -sf http://localhost:11434/api/version >/dev/null 2>&1 && break
    sleep 1
  done
fi

# 2. Ensure the model is available locally (no-op if already pulled).
echo "==> Ensuring $LICENTA_MODEL is pulled…"
ollama pull "$LICENTA_MODEL"

# 3. Start Streamlit in the background and wait for the port.
echo "==> Starting Streamlit…"
uv run streamlit run streamlit_app.py \
  --server.port "$PORT" --server.headless true \
  >/tmp/licenta_streamlit.log 2>&1 &
ST_PID=$!
trap 'echo; echo "==> stopping…"; kill "$ST_PID" 2>/dev/null || true; exit 0' INT TERM
for _ in $(seq 1 40); do
  curl -sf "http://localhost:$PORT" >/dev/null 2>&1 && break
  sleep 1
done
echo "==> Streamlit up on http://localhost:$PORT (logs: /tmp/licenta_streamlit.log)"

# 4. Open the public tunnel in the foreground — the trycloudflare.com URL prints below.
echo "==> Opening Cloudflare tunnel. Share the https://*.trycloudflare.com URL it prints:"
cloudflared tunnel --url "http://localhost:$PORT"
