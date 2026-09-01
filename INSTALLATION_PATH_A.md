# Ruflo Installation — Path A (Claude Code Plugins)

**Lightweight setup via Claude Code plugin marketplace.**

## Prerequisites

- Claude Code (web, CLI, or IDE extension)
- Internet connection
- Active Claude Code session

## Installation Steps

### Step 1: Add Marketplace

In Claude Code, run:
```
/plugin marketplace add ruvnet/ruflo
```

This registers the Ruflo plugin marketplace.

### Step 2: Install Core Plugin

```
/plugin install ruflo-core@ruflo
```

**What it adds:**
- Slash commands for Ruflo operations
- Agent definitions (98+ types)
- MCP server registration
- Health checks and discovery

### Step 3: (Optional) Install Additional Plugins

Choose based on your needs:

```bash
# Swarm coordination
/plugin install ruflo-swarm@ruflo

# Memory and RAG
/plugin install ruflo-rag-memory@ruflo
/plugin install ruflo-agentdb@ruflo

# Workflows and automation
/plugin install ruflo-workflows@ruflo
/plugin install ruflo-loop-workers@ruflo

# Advanced features
/plugin install ruflo-federation@ruflo
/plugin install ruflo-neural-trader@ruflo
```

## Verify Installation

Check that Ruflo is available:

```
/help ruflo
```

Or list installed plugins:

```
/plugin list
```

## Available Slash Commands (Post-Install)

| Command | Purpose |
|---------|---------|
| `/ruflo init` | Initialize Ruflo in current project |
| `/ruflo agent spawn` | Create a new agent |
| `/ruflo swarm start` | Coordinate multiple agents |
| `/ruflo memory store` | Save to agent memory |
| `/ruflo memory search` | Query agent memory |
| `/ruflo status` | System health check |
| `/ruflo doctor` | Diagnostics |

## MCP Tools Available

After ruflo-core install, these MCP tools are callable:

- `mcp__plugin_ruflo-core_ruflo__agent_spawn`
- `mcp__plugin_ruflo-core_ruflo__memory_store`
- `mcp__plugin_ruflo-core_ruflo__memory_search`
- `mcp__plugin_ruflo-core_ruflo__swarm_init`
- `mcp__plugin_ruflo-core_ruflo__status`

**Note:** Tool names use `mcp__plugin_ruflo-core_ruflo__*` prefix (not bare names like the CLI path).

## Next Steps

1. ✅ Install ruflo-core
2. Run `/ruflo init` to configure current project
3. Explore agent types with `/help agents`
4. Try spawning an agent: `/ruflo agent spawn -t coder`
5. Monitor with `/ruflo status --watch`

## Troubleshooting

### Command not found
- Ensure ruflo-core plugin finished installing
- Restart Claude Code session
- Check `/plugin list` for ruflo-core status

### MCP tools unavailable
- ruflo-core registers its own MCP server
- Other plugins may not include MCP tools
- Use slash commands as primary interface

### Missing features
- Path A provides slash commands + basic features
- For full CLI (26+ commands, daemon, hooks), use Path B: `npx ruflo init`

## Uninstall

```
/plugin uninstall ruflo-core@ruflo
```

---

**Installation Date**: 2026-09-01  
**Method**: Plugin Marketplace (Path A)  
**Status**: Ready for configuration
