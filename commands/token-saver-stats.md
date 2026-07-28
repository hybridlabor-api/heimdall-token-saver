---
name: stats
description: "Show token-saver compression statistics and savings"
---

Run the heimdall stats command to display savings:

```bash
heimdall stats
```

If the `token-saver` CLI is not in PATH, use:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/src/cli.py" stats
```

Present a summary of tokens saved in the current session and overall.
