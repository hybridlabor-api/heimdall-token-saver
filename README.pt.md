![Heimdall Token Saver](header.png)

🌐 **Idioma / Language / Sprache**: [ 🇬🇧 English ](README.md) | [ 🇩🇪 Deutsch ](README.de.md) | **Português**

---

# Heimdall Token Saver

[![CI](https://github.com/hybridlabor-api/heimdall-token-saver/actions/workflows/ci.yml/badge.svg)](https://github.com/hybridlabor-api/heimdall-token-saver/actions)
[![NPM Version](https://img.shields.io/npm/v/@hybridlabor-api/heimdall-token-saver.svg)](https://www.npmjs.com/package/@hybridlabor-api/heimdall-token-saver)
[![runtime](https://img.shields.io/badge/python-3.9+-blue.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)
[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![savings](https://img.shields.io/badge/avg%20savings-60%25--99%25-brightgreen.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)

**Economize mais tokens e obtenha mais de 60% de capacidade adicional de código na sua assinatura de IA (Claude Code, Codex, Antigravity).**

---

## ⚡ POR QUE HEIMDALL // Reduza seus custos de IA em 60-99% em saídas CLI

Assinaturas de código com IA (**Claude Code, OpenAI Codex / ChatGPT, Google Antigravity**) são limitadas por tamanhos de janela de contexto e limites horários rígidos. Toda vez que seu agente executa um comando de terminal — `git diff`, `pytest`, `npm install`, `docker`, `terraform plan` ou `kubectl` — mais de **90% da saída bruta é ruído puro** (barras de progresso, testes aprovados, spinners e textos de lockfile).

### O Problema com Saídas Brutas do Terminal
Quando um agente de IA lê logs brutos da CLI:
1. **Desperdício de cotas de assinatura:** Seus limites de taxa expiram até **5x mais rápido** porque o modelo lê milhares de linhas inúteis.
2. **Poluição da janela de contexto:** A memória de trabalho do modelo fica sobrecarregada com texto irrelevante, fazendo o agente esquecer instruções anteriores.
3. **Custos de API mais altos:** Se você paga por 1M de tokens, cada execução consome dinheiro desnecessariamente.

### A Solução Heimdall
**Heimdall Token Saver** atua como um firewall de contexto local inteligente e de latência zero:
- 🛡 **100% Sinal, 0% Ruído:** Remove barras de progresso e logs bem-sucedidos garantindo **zero perda de informação**. Todos os erros, rastreamentos de pilha e diffs permanecem intactos.
- 🚀 **Valor Máximo de Assinatura:** Oferece **mais de 60% de capacidade efetiva de contexto**.
- ⚡ **Respostas Mais Rápidas:** Menos texto para o LLM ler significa respostas mais rápidas e foco preciso na depuração.

---

### Economia Antes & Depois

| Comando / Ferramenta MCP | Saída Bruta | Saída Comprimida | Economia de Tokens |
|-------------------|-----------|-------------------|---------------|
| `git diff` (grande refatoração) | 2.270 tokens | 909 tokens | **60%** |
| `pytest` (500 testes, 2 falhas) | 6.744 tokens | 308 tokens | **95%** |
| `npm install` (220 pacotes) | 3.844 tokens | 4 tokens | **99%** |
| `bdb_td_nodes` (Dump TouchDesigner) | 12.400 tokens | 620 tokens | **95%** |
| `bdb_unreal_actor` (Unreal Engine PCG) | 8.900 tokens | 445 tokens | **95%** |
| `bdb_after_effects` (AE keyframes) | 6.500 tokens | 455 tokens | **93%** |
| `bdb_davinci_timeline` (Dump Resolve) | 9.100 tokens | 728 tokens | **92%** |
| `memb_search_memory` (Busca memB) | 5.400 tokens | 324 tokens | **94%** |

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
 │   36 Processadores Locais Especializados (Zero Latência)│
 └───────────────────────────┬────────────────────────────┘
                             │
            ┌────────────────┴────────────────┐
            │                                 │
            ▼                                 ▼
   ┌─────────────────┐               ┌──────────────────┐
   │ PRESERVADO(100%)│               │ DESCARTADO (0%)  │
   │ • Erros & Traces│               │ • Progresso      │
   │ • Testes Falhos │               │ • Testes Ok      │
   │ • Diffs         │               │ • Logs Download  │
   └────────┬────────┘               └──────────────────┘
            │
            ▼
 🎯 RESULTADO: 60-99% de Redução de Tokens!
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
