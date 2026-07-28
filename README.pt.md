![Heimdall Token Saver](header.png)

🌐 **Idioma / Language / Sprache**: [ 🇬🇧 English ](README.md) | [ 🇩🇪 Deutsch ](README.de.md) | **Português**

---

# Heimdall Token Saver

[![CI](https://github.com/hybridlabor-api/heimdall-token-saver/actions/workflows/ci.yml/badge.svg)](https://github.com/hybridlabor-api/heimdall-token-saver/actions)
[![NPM Version](https://img.shields.io/npm/v/@hybridlabor-api/heimdall-token-saver.svg)](https://www.npmjs.com/package/@hybridlabor-api/heimdall-token-saver)
[![runtime](https://img.shields.io/badge/python-3.9+-blue.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)
[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![savings](https://img.shields.io/badge/avg%20savings-60%25--99%25-brightgreen.svg)](https://github.com/hybridlabor-api/heimdall-token-saver)

**Economize tokens e obtenha mais de 60% de capacidade adicional de código na sua assinatura de IA (Claude Code, Codex, Antigravity).**

---

## ⚡ POR QUE HEIMDALL // Reduza seus custos de IA em 60-99% em saídas CLI

Assinaturas de código com IA (**Claude Code, OpenAI Codex, Google Antigravity**) são limitadas por tamanhos de janela de contexto e limites horários rígidos. Toda vez que seu agente executa um comando de terminal — `git diff`, `pytest`, `npm install`, `docker`, `terraform plan` ou `kubectl` — mais de **90% da saída bruta é ruído**.

### O Problema com Saídas Brutas do Terminal
1. **Desperdício de cota de assinatura:** Seus limites de taxa expiram até **5x mais rápido**.
2. **Poluição da janela de contexto:** A memória de trabalho do modelo fica desorganizada com texto irrelevante.
3. **Custos de API mais altos:** Cada execução consome tokens desnecessários em testes aprovados e barras de progresso.

### A Solução Heimdall
**Heimdall Token Saver** atua como um firewall de contexto local inteligente e de latência zero:
- 🛡 **100% Sinal, 0% Ruído:** Remove barras de progresso e logs bem-sucedidos garantindo **zero perda de informação**. Todos os erros, rastreamentos de pilha e diffs permanecem intactos.
- 🚀 **Valor Máximo de Assinatura:** Oferece **mais de 60% de capacidade efetiva de contexto**.
- ⚡ **Respostas Mais Rápidas:** Menos texto para o LLM ler significa respostas mais rápidas e foco preciso no depuramento.

---

## 🛠️ INSTALAÇÃO RÁPIDA

```bash
# Instalar e ativar via NPX
npx @hybridlabor-api/heimdall-token-saver@latest --target antigravity
```

---

## 📚 DOCUMENTAÇÃO

Para referências de comandos completas, configurações de processadores e benchmarks, consulte o diretório [.openwiki/](.openwiki/quickstart.md).
