# 📐 Heimdall Token Saver – System Architecture

This document outlines the architecture, compression pipeline, and agent integration layers of **Heimdall Token Saver**.

---

## 🏛️ System Overview

Heimdall Token Saver is an ultra-fast context compression engine designed to intercept and compress verbose CLI tool outputs before they enter AI coding agent context windows (Claude Code, OpenAI Codex, Google Antigravity, Cursor, Windsurf).

```text
┌─────────────────────────────────────────────────────────────┐
│                 CLI Command Execution                       │
│    (git diff, pytest, npm test, docker, cargo, terraform)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
               ┌───────────────────────────────┐
               │  Heimdall Interceptor Engine  │
               │  - Rule Matcher & Tokenizer   │
               │  - Specialized Processors     │
               │  - Noise & Spinner Stripper   │
               └───────────────┬───────────────┘
                               │ (60% - 99% Compression)
                               ▼
               ┌───────────────────────────────┐
               │    Clean Compressed Context   │
               │  - High-Signal Diff / Errors  │
               │  - Token Savings Metrics      │
               │  - Fed to LLM Context Window  │
               └───────────────────────────────┘
```

---

## 📦 Core Subsystems

### 1. Interceptor & CLI Wrapper (`src/cli.py`, `bin/token-saver`)
- High-performance command line interface wrapping arbitrary terminal invocations.
- Measures raw token volume vs compressed token output in real-time.

### 2. Specialized Processors (`src/processors/`)
- **Git Processor:** Strips binary blobs, large lockfiles, and repetitive metadata while preserving semantic hunk changes.
- **Test Runner Processors (Pytest, Jest, Vitest, Go Test, Cargo Test):** Eliminates passing test spam; isolates failing stack traces, assert comparisons, and panic logs.
- **Package Manager Processors (NPM, Yarn, Pip, Cargo):** Strips animated spinners, progress bars, and transient dependency notices.
- **Infrastructure Processors (Docker, Terraform, Kubectl):** Compresses resource state listings into dense, agent-digestible summaries.

### 3. Statistics & Tracking (`src/stats.py`, `src/tracker.py`)
- Persistent metrics storage tracking cumulative tokens saved, session efficiency, and dollar savings.

### 4. Harness & Platform Installers (`installers/`, `skills/`)
- Automated installer scripts for Antigravity, Claude Code, Cursor, Codex, and Windsurf.
- Exposes native Antigravity skill `token-saver-config`.

---

## 🔗 Role in BDB Ecosystem

Heimdall Token Saver ensures that all multi-agent coding sessions run with maximum token efficiency, preventing context window bloat and extending agent session longevity.
