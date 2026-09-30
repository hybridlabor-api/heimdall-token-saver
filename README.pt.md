![Heimdall Token Saver](header.png)

🌐 **Idioma / Language / Sprache**: [ 🇬🇧 English ](README.md) | [ 🇩🇪 Deutsch ](README.de.md) | **Português**

---

# Heimdall Token Saver

[![CI](https://github.com/hybridlabor-api/heimdall-token-saver/actions/workflows/ci.yml/badge.svg)](https://github.com/hybridlabor-api/heimdall-token-saver/actions)
[![NPM Version](https://img.shields.io/npm/v/@hybridlabor-api/heimdall-token-saver.svg)](https://www.npmjs.com/package/@hybridlabor-api/heimdall-token-saver)
[![runtime](https://img.shields.io/badge/python-3.9+-blue.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)
[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![savings](https://img.shields.io/badge/savings-see%20fixtures-lightgrey.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)

**Comprima a saída ruidosa de CLI antes que chegue ao seu agente de IA (Claude Code, Codex, Antigravity) para economizar tokens de contexto.**

---

## ⚡ POR QUE HEIMDALL // Reduza tokens em saídas CLI ruidosas

Assinaturas de código com IA (**Claude Code, OpenAI Codex / ChatGPT, Google Antigravity**) são limitadas por tamanhos de janela de contexto e limites horários rígidos. Toda vez que seu agente executa um comando de terminal — `git diff`, `pytest`, `npm install`, `docker`, `terraform plan` ou `kubectl` — boa parte da saída bruta costuma ser ruído (barras de progresso, testes aprovados, spinners e textos de lockfile).

### O Problema com Saídas Brutas do Terminal
Quando um agente de IA lê logs brutos da CLI:
1. **Desperdício de cotas de assinatura:** Seus limites de taxa expiram até **5x mais rápido** porque o modelo lê milhares de linhas inúteis.
2. **Poluição da janela de contexto:** A memória de trabalho do modelo fica sobrecarregada com texto irrelevante, fazendo o agente esquecer instruções anteriores.
3. **Custos de API mais altos:** Se você paga por 1M de tokens, cada execução consome dinheiro desnecessariamente.

### A Solução Heimdall
**Heimdall Token Saver** atua como um firewall de contexto local inteligente e de latência zero:
- 🛡 **Remoção de ruído com perda limitada:** Remove barras de progresso e logs bem-sucedidos. A compressão tem perdas: trechos longos no meio podem perder linhas (inclusive erros). Veja o README em inglês.
- 🚀 **Menos contexto usado:** A economia depende do comando; nenhum número geral é garantido.
- ⚡ **Respostas Mais Rápidas:** Menos texto para o LLM ler significa respostas mais rápidas e foco preciso na depuração.

---

### Economia Antes & Depois

A tabela anterior (60-99%) não tinha fixtures nem benchmark e foi removida. Números reproduzíveis de `examples/fixtures/` (`python3 examples/demo.py`) estão no [README](README.md#before--after-savings) em inglês; os processadores BDB MCP não têm fixtures nem benchmark.

---

## 🛠️ COMO FUNCIONA

```
 ┌────────────────────────────────────────────────────────┐
 │           Saída Bruta do Comando de Terminal           │
 │    (git diff, pytest, npm install, docker, terraform)   │
 └───────────────────────────┬────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │            MOTOR HEIMDALL TOKEN SAVER                  │
 │   42 Processadores Locais Especializados (Zero Latência)│
 └───────────────────────────┬────────────────────────────┘
                             │
            ┌────────────────┴────────────────┐
            │                                 │
            ▼                                 ▼
   ┌─────────────────┐               ┌──────────────────┐
   │ PRESERVADO      │               │ DESCARTADO        │
   │ • Erros & Traces│               │ • Progresso      │
   │ • Testes Falhos │               │ • Testes Ok      │
   │ • Diffs         │               │ • Logs Download  │
   └────────┬────────┘               └──────────────────┘
            │
            ▼
 🎯 RESULTADO: menos tokens por comando (varia por comando)
```

---

## 🚀 Instalação & Uso

```bash
# Método recomendado via NPX
npx -y @hybridlabor-api/heimdall-token-saver
```

---

## 📄 Licença

[Apache 2.0](LICENSE) © Hybridlabor / BDB DEV
