# Ruflo Setup Guide

## Overview

Ruflo is an agent meta-harness for Claude Code and Codex. This setup guide configures the development environment and installation paths.

## Installation Status

### Issue: Private Dependencies

The direct `npm install` fails due to private packages (`@claude-flow/mcp` and related):

```
npm error 403 403 Forbidden - GET https://registry.npmjs.org/@claude-flow%2fmcp
```

**Solution**: Use the CLI installation path instead.

## Installation Paths

### Path A: Claude Code Plugins (Recommended for Quick Setup)

1. Add the marketplace:
```bash
/plugin marketplace add ruvnet/ruflo
```

2. Install core plugin:
```bash
/plugin install ruflo-core@ruflo
```

3. Optional: Install additional plugins:
```bash
/plugin install ruflo-swarm@ruflo
/plugin install ruflo-rag-memory@ruflo
```

**Benefits**:
- Zero files in workspace
- Slash commands available immediately
- Lower footprint

### Path B: Full CLI Installation (Production)

```bash
# From ruflo directory
npx ruflo init --wizard
```

This provides:
- 98+ specialized agents
- 60+ CLI commands
- 30+ skills
- Hooks system
- MCP server
- Daemon process

## Project Structure

```
cyberskills-ecc/
├── README.md
├── RUFLO_SETUP.md (this file)
└── ruflo/                    # Cloned from ruvnet/ruflo
    ├── v3/                   # Claude Flow V3 (modular architecture)
    ├── plugins/              # 35+ available plugins
    ├── .claude/              # Claude Code configuration
    ├── CLAUDE.md             # Detailed project documentation
    └── package.json          # Monorepo with workspaces
```

## Key Components

| Component | Path | Purpose |
|-----------|------|---------|
| Core CLI | `v3/@claude-flow/cli/` | 26 commands, 140+ subcommands |
| Codex Bridge | `v3/@claude-flow/codex/` | Dual-mode Claude + Codex collaboration |
| Memory System | `v3/@claude-flow/memory/` | AgentDB + HNSW vector search |
| Security | `v3/@claude-flow/security/` | Input validation, CVE remediation |
| Guidance | `v3/@claude-flow/guidance/` | Governance control plane |

## Quick Commands

```bash
# Initialize with wizard
npx ruflo init

# Start daemon
npx ruflo daemon start

# Spawn an agent
npx ruflo agent spawn -t coder --name my-coder

# System health check
npx ruflo doctor

# Search memory
npx ruflo memory search -q "pattern query"
```

## Development Workflow

1. Clone ruflo: ✅ Complete
2. Configure agents: `npx ruflo init`
3. Start daemon: `npx ruflo daemon start`
4. Create agents: `npx ruflo agent spawn ...`
5. Monitor: `npx ruflo status --watch`

## Next Steps

- [ ] Choose installation path (A or B)
- [ ] Run installation command
- [ ] Verify with `npx ruflo doctor`
- [ ] Explore available agents: `npx ruflo agent list`
- [ ] Read CLAUDE.md for advanced configuration

## References

- [Ruflo on npm](https://www.npmjs.com/package/ruflo)
- [GitHub](https://github.com/ruvnet/ruflo)
- [Documentation](https://github.com/ruvnet/ruflo/blob/main/CLAUDE.md)
- [UI Beta](https://flo.ruv.io/)

## Notes

- Private npm packages require authentication for full CLI install
- Plugin marketplace path (A) works without authentication
- MCP server included with CLI path (B)
- Hooks system for automation available with full install

---

**Setup Date**: 2026-09-01  
**Branch**: `claude/ruflo-setup-kzr33a`
