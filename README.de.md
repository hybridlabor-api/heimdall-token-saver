![Heimdall Token Saver](header.png)

🌐 **Sprache / Language / Idioma**: [ 🇬🇧 English ](README.md) | **Deutsch** | [ 🇵🇹 Português ](README.pt.md)

---

# Heimdall Token Saver

[![CI](https://github.com/hybridlabor-api/heimdall-token-saver/actions/workflows/ci.yml/badge.svg)](https://github.com/hybridlabor-api/heimdall-token-saver/actions)
[![NPM Version](https://img.shields.io/npm/v/@hybridlabor-api/heimdall-token-saver.svg)](https://www.npmjs.com/package/@hybridlabor-api/heimdall-token-saver)
[![runtime](https://img.shields.io/badge/python-3.9+-blue.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)
[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![savings](https://img.shields.io/badge/savings-see%20fixtures-lightgrey.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)

**Spare mehr Token & erhalte über 60 % mehr Coding-Power aus deinem KI-Abonnement (Claude Code, Codex, Antigravity).**

---

## ⚡ WARUM HEIMDALL // Reduziere deine KI-Coding-Kosten um 60–99 % bei CLI-Ausgaben

KI-Coding-Abonnements (**Claude Code, OpenAI Codex / ChatGPT, Google Antigravity**) sind durch Context-Window-Größen und stündliche Limits beschränkt. Jedes Mal, wenn dein KI-Agent einen Terminal-Befehl ausführt — `git diff`, `pytest`, `npm install`, `docker`, `terraform plan` oder `kubectl` — sind über **90 % der Rohausgabe reiner Lärm** (Fortschrittsbalken, bestandene Tests, Spinner und Lockfile-Text).

### Das Problem mit roher Terminal-Ausgabe
Wenn ein KI-Agent rohe CLI-Logs liest:
1. **Du verschwendest deine Abonnement-Quotas:** Deine 5-Stunden-Limits laufen bis zu **5x schneller** ab, weil das Modell Tausende Zeilen unnötiger Fortschrittsbalken liest.
2. **Kontextfenster-Verschmutzung:** Das Arbeitsgedächtnis des LLMs wird mit irrelevantem Boilerplate zugemüllt, wodurch der Agent frühere Anweisungen vergisst und fehlerhafte Fixes halluziniert.
3. **Höhere API-Kosten:** Wenn du pro 1M Token zahlst, verbrennt jeder `pytest`- oder `npm install`-Durchlauf Geld für bestandene Tests und Ladeindikatoren.

### Die Heimdall-Lösung
**Heimdall Token Saver** agiert als intelligente, verzögerungsfreie lokale Kontext-Firewall zwischen deinen CLI-Tools und deinem KI-Agenten:
- 🛡 **Rauschentfernung mit begrenztem Verlust:** Strippt Fortschrittsbalken, bestandene Test-Logs und Spinner. Die Komprimierung ist verlustbehaftet: Sehr lange Mittelteile können Zeilen (auch Fehler) verlieren, siehe Präzisionshinweise unten und den englischen README.
- 🚀 **Weniger Kontextverbrauch:** Die Ersparnis hängt vom Befehl ab; es wird keine pauschale Zahl behauptet.
- ⚡ **Schnellere Antworten:** Weniger Text für das LLM bedeutet schnellere Antwortzeiten und einen messerscharfen Debugging-Fokus.

---

### Ersparnisse Vorher & Nachher

Die frühere Tabelle (60-99 %, 90-95 % pro MCP-Aufruf) war nicht durch Fixtures oder Benchmarks belegt und wurde entfernt. Reproduzierbare Zahlen aus `examples/fixtures/` (`python3 examples/demo.py`) stehen im englischen [README](README.md#before--after-savings); für die BDB-MCP-Prozessoren gibt es keine Fixtures oder Benchmarks.

> Führe `heimdall benchmark <befehl>` aus, um Ersparnisse in Echtzeit für deine eigenen Workloads zu messen.

---

## 🛠️ WIE ES FUNKTIONIERT

Heimdall Token Saver sitzt transparent zwischen deinen Terminal-Befehlen und deinen KI-Coding-Assistenten (**Claude Code, OpenAI Codex, Antigravity CLI**).

### Visueller Pipeline-Ablauf

```
 ┌────────────────────────────────────────────────────────┐
 │           Rohe CLI-Befehlsausgabe                      │
 │    (git diff, pytest, npm install, docker, terraform)   │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │            HEIMDALL TOKEN SAVER ENGINE                 │
 │   42 Spezialisierte Lokale Prozessoren (Null Latenz)   │
 └───────────────────────────┬────────────────────────────┘
                             │
            ┌────────────────┴────────────────┐
            │                                 │
            ▼                                 ▼
   ┌─────────────────┐               ┌──────────────────┐
   │ BEHALTEN        │               │ VERWORFEN         │
   │ • Fehler-Traces │               │ • Fortschrittsbal│
   │ • Fehlgeschl.   │               │ • Bestandene Test│
   │ • Datei-Diffs   │               │ • Download-Logs  │
   │ • Warnungen     │               │ • Boilerplate    │
   └────────┬────────┘               └──────────────────┘
            │
            ▼
 ┌────────────────────────────────────────────────────────┐
 │       Saubere, Komprimierte Kontext-Ausgabe            │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │       KI-Coding-Assistenten & Abonnements              │
 │     (Claude Code • OpenAI Codex • Antigravity CLI)     │
 └────────────────────────────────────────────────────────┘
            │
            ▼
 🎯 ERGEBNIS: weniger Tokens pro Befehl (je nach Befehl unterschiedlich)
```

### Architektur & Engine-Mechanik

```
CLI-Befehl  -->  Spezialisierter Prozessor  -->  Komprimierte Ausgabe
                         |
                   42 Prozessoren
                   (git, test, cargo, go, build,
                    lint, package_list, python_install,
                    maven_gradle, bun, network, docker,
                    kubectl, terraform, pulumi, cdktf,
                    nix, mise, env, search, system_info,
                    gh, db_query, cloud_cli, ansible,
                    helm, syslog, ssh, jq_yq, just, act,
                    structured_log, file_listing,
                    file_content, generic)
```

Die Engine (`CompressionEngine`) verwaltet eine priorisierte Kette von Prozessoren. Der erste Prozessor, der den Befehl verarbeiten kann (`can_handle()`), erzeugt die komprimierte Ausgabe. `GenericProcessor` dient als Fallback.

### Plattform-Integration

**Claude Code** (PreToolUse Hook):
Rewritet Befehle zu `python3 wrap.py '<befehl>'`, um die Ausgabe vor dem Lesen zu komprimieren.

**Antigravity CLI** (AfterTool Hook):
Ersetzt Ausgaben direkt über den native Deny/Reason-Mechanismus.

### Präzisionsgarantien

Die Komprimierung ist verlustbehaftet; es gibt **keine** Garantie für null Informationsverlust.

- Getestet (`tests/test_precision.py`): u. a. Dateinamen/Änderungen in Diffs, Commit-Hashes, fehlgeschlagene Tests samt Stacktrace, Fehlerzeilen, `env`-Secrets werden anonymisiert; bei generischer Kürzung bleiben Anfang und Ende erhalten und ein Marker `... (N lines truncated, M total) ...` wird eingefügt.
- Grenzen: Lange Mittelteile können Zeilen verlieren, auch Fehler (generisch: Standard 100 Kopf- + 50 Endzeilen ab 200 Zeilen). Tracebacks sind auf 30 Zeilen (`max_traceback_lines`), Diff-Hunks auf 50 Zeilen (`max_diff_hunk_lines`) begrenzt.
- Nur Bash-Befehle werden gehookt (Matcher `Bash`); MCP-Tool-Aufrufe laufen nicht durch Heimdall. Der Hook liefert `permissionDecision: "allow"` für umgeschriebene Befehle.
- Quellcode-Dateien (`cat *.py`, `cat *.ts`) passieren **unverändert**.
- Details und Standardwerte: englischer [README](README.md).

---

## 🚀 Installation & Setup

### Voraussetzungen
- Python 3.10+
- Claude Code und/oder Antigravity CLI

### Methode 1: Claude Code Plugin (Empfohlen)
```bash
/plugin marketplace add hybridlabor-api/heimdall-token-saver
/plugin install token-saver
```

### Methode 2: Manuelle Installation
```bash
git clone https://github.com/hybridlabor-api/heimdall-token-saver.git
cd token-saver
python3 install.py --target claude        # Nur Claude Code
python3 install.py --target antigravity   # Nur Antigravity CLI
python3 install.py --target both         # Beide Plattformen
```

### Methode 3: Via NPX (Globaler Installer)
```bash
npx -y @hybridlabor-api/heimdall-token-saver
```

---

## 🔌 Spezialisierte BDB MCP Prozessoren (70–95 % Ersparnis)

1. **BdbTouchdesignerProcessor**: Komprimiert Node-Graph Dumps, Cook-Logs und DAT-Skripte.
2. **BdbUnrealProcessor**: Komprimiert Unreal Engine 5 Logs, PCG-Graphen und Actor-Transforms.
3. **BdbAfterEffectsProcessor**: Komprimiert ExtendScript-Fehler und Layer-Arrays.
4. **BdbDavinciProcessor**: Komprimiert Timeline-Schnitt-Dumps und Render-Jobs.
5. **BdbCreativeSuiteProcessor**: Komprimiert Resolume, Rhino 3D, Photoshop & Vectorworks Dumps.
6. **BdbMembProcessor**: Komprimiert memB Vektorspeicher-Antworten und strippt riesige Float-Arrays.

---

## ⚙️ Konfiguration

Werte können über `~/.token-saver/config.json` oder Umgebungsvariablen (`TOKEN_SAVER_*`) angepasst werden:

```json
{
  "enabled": true,
  "min_input_length": 200,
  "min_compression_ratio": 0.10,
  "max_diff_hunk_lines": 150,
  "max_log_entries": 20,
  "max_file_lines": 300,
  "generic_truncate_threshold": 500,
  "debug": false
}
```

---

## 📊 CLI & Statistiken

Nach der Installation steht der Befehl `heimdall` / `token-saver` zur Verfügung:

```bash
heimdall version              # Ausführung der aktuellen Version anzeigen
heimdall stats                # Kumulierte Token- & Kostenersparnis anzeigen
heimdall stats --json         # JSON-Statistik exportieren
heimdall benchmark 'git diff' # Komprimierungsrate für jeden CLI-Befehl messen
heimdall update               # Automatisch Updates prüfen und anwenden
```

---

## 📄 Lizenz

[Apache 2.0](LICENSE) © Hybridlabor / BDB DEV
