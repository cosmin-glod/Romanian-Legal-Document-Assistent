#!/usr/bin/env bash
# Demo launcher: UI + retrieval + Chroma index run LOCALLY; GENERATION runs on a
# REMOTE Ollama endpoint (best model, e.g. 14B). If the endpoint is unreachable or
# missing the model, it AUTO-FALLS-BACK to a local 3B-Q8 so the demo never dies.
#
#   Kaggle test:   OLLAMA_HOST=https://xxxx.trycloudflare.com ./scripts/demo_remote.sh
#   RunPod (talk): OLLAMA_HOST=https://<pod-id>-11434.proxy.runpod.net ./scripts/demo_remote.sh
#   No endpoint:   ./scripts/demo_remote.sh            # goes straight to local 3B-Q8
#
# Endpoint notebook: kaggle/ollama_endpoint.ipynb (serves qwen2.5:14b + cloudflared tunnel).
# Env: OLLAMA_HOST, LICENTA_MODEL (remote, default 14B), FALLBACK_MODEL (default 3B-Q8), PORT.
#
# --- RunPod setup (presentation) -------------------------------------------
#  1. Pod with >=16 GB GPU (L4/A4000/A10) + Ollama (template, or install via curl).
#  2. On pod:  ollama serve &   then   ollama pull qwen2.5:14b-instruct-q4_K_M
#  3. Expose HTTP 11434 -> URL https://<pod-id>-11434.proxy.runpod.net
#  4. Run this script locally with that URL. Tear pod down after.
# ---------------------------------------------------------------------------
set -euo pipefail
cd "$(dirname "$0")/.."

REMOTE_HOST="${OLLAMA_HOST:-}"
REMOTE_MODEL="${LICENTA_MODEL:-qwen2.5:14b-instruct-q4_K_M}"
FALLBACK_MODEL="${FALLBACK_MODEL:-qwen2.5:3b-instruct-q8_0}"
PORT="${PORT:-8501}"

endpoint_ok() {
  [ -n "$REMOTE_HOST" ] || return 1
  curl -sf --max-time 8 "$REMOTE_HOST/api/version" >/dev/null 2>&1 || return 1
  curl -sf --max-time 8 "$REMOTE_HOST/api/tags" 2>/dev/null | grep -q "${REMOTE_MODEL%%:*}" || return 1
}

if endpoint_ok; then
  echo "==> REMOTE endpoint OK: $REMOTE_MODEL @ $REMOTE_HOST"
  export OLLAMA_HOST="$REMOTE_HOST"
  export LICENTA_MODEL="$REMOTE_MODEL"
else
  [ -n "$REMOTE_HOST" ] && echo "==> endpoint unreachable/model missing -> FALLBACK to local $FALLBACK_MODEL" \
                        || echo "==> no OLLAMA_HOST set -> local $FALLBACK_MODEL"
  unset OLLAMA_HOST                       # ollama lib defaults to 127.0.0.1:11434
  export LICENTA_MODEL="$FALLBACK_MODEL"
  if ! curl -sf http://localhost:11434/api/version >/dev/null 2>&1; then
    echo "   starting local 'ollama serve'..."
    ollama serve >/tmp/licenta_ollama.log 2>&1 &
    for _ in $(seq 1 30); do curl -sf http://localhost:11434/api/version >/dev/null 2>&1 && break; sleep 1; done
  fi
  echo "   ensuring $FALLBACK_MODEL is pulled (one-time)..."
  ollama pull "$FALLBACK_MODEL"
fi

echo "==> UI: http://localhost:$PORT   (model: $LICENTA_MODEL)"
echo "    if the endpoint dies mid-demo: Ctrl-C and re-run -> auto-fallback to local."
uv run streamlit run streamlit_app.py --server.port "$PORT"
