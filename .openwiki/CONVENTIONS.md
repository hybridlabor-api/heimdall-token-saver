# 📋 Heimdall Token Saver – Development Conventions

This document defines coding standards, testing rules, and packaging conventions for **Heimdall Token Saver**.

---

## 🛠️ Python & Tooling Conventions

- **Target Runtime:** Python 3.9+ (strictly typed with `mypy` annotations).
- **Code Quality:** Format and lint with `ruff`.
- **Zero-Loss Compression:** Processors must NEVER drop critical compiler errors, failing test assertions, or file path references. Only decorative noise and redundant progress indicators may be stripped.
- **Performance Budget:** Interception and regex processing must add `< 10ms` latency to CLI commands.

---

## 🧪 Testing & Verification

- **Pytest Suite:** All processor logic must be validated against real-world test logs in `tests/`.
- Run test suite locally:
  ```bash
  pytest tests/ -v
  ```

---

## 🌿 Git & Release Workflow

- **Branching:** Main branch `main` is production-ready.
- **Commit Messages:** Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
- **Semantic Versioning:** Version bump in both `pyproject.toml` and `package.json` for NPM / PyPI distribution parity.
