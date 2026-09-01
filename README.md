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

## 🔗 Resources

- [Ruflo on npm](https://www.npmjs.com/package/ruflo)
- [GitHub Repository](https://github.com/ruvnet/ruflo)
- [UI Beta](https://flo.ruv.io/)
- [Detailed Documentation](https://github.com/ruvnet/ruflo/blob/main/CLAUDE.md)