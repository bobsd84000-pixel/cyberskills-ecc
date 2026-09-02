# cyberskills-ecc

Development environment for Ruflo (Claude Flow V3) — agent meta-harness for Claude Code and Codex.

## 🚀 Quick Start

**Path A (Recommended)**: Claude Code Plugins
```bash
./scripts/install-path-a.sh
```
Or manually: `/plugin marketplace add ruvnet/ruflo` → `/plugin install ruflo-core@ruflo`

**Path B**: Full CLI (requires authentication)
```bash
npx ruflo init --wizard
```

## 🔌 Marketplace de plugins (ce dépôt)

Ce dépôt est aussi une marketplace de plugins Claude Code. Il fournit le plugin `anthropic-pack` (skills `caveman` et `task-observer`).

```
/plugin marketplace add bobsd84000-pixel/cyberskills-ecc
/plugin install anthropic-pack@cyberskills-ecc
```

## 📚 Documentation

| File | Purpose |
|------|---------|
| [RUFLO_SETUP.md](./RUFLO_SETUP.md) | Overview, installation paths, troubleshooting |
| [INSTALLATION_PATH_A.md](./INSTALLATION_PATH_A.md) | Detailed Path A guide with MCP tools reference |
| [scripts/install-path-a.sh](./scripts/install-path-a.sh) | Automated installation script |

## 📦 Project Contents

- `ruflo/` — External clone from [ruvnet/ruflo](https://github.com/ruvnet/ruflo) (git-ignored)
- `scripts/` — Installation and utility scripts
- `.gitignore` — Configured for external dependencies

## ✨ Features

After installation:
- 98+ specialized agents
- Slash commands in Claude Code
- Agent coordination and swarms
- Memory and RAG systems
- MCP server integration

## 📊 Dashboards

- [Économie de tokens](https://claude.ai/code/artifact/b9a98b68-ba61-4d60-9703-312dfc82971c) — usage réel de tokens (neuf vs cache), coût et économie réalisée

## 🔗 Resources

- [Ruflo on npm](https://www.npmjs.com/package/ruflo)
- [GitHub Repository](https://github.com/ruvnet/ruflo)
- [UI Beta](https://flo.ruv.io/)
- [Detailed Documentation](https://github.com/ruvnet/ruflo/blob/main/CLAUDE.md)