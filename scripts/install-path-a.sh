#!/bin/bash
# Ruflo Path A Installation Script
# Installs Ruflo plugins via Claude Code marketplace
# Supports both interactive and non-interactive modes

set -e

# Detect if running interactively
INTERACTIVE=false
if [[ -t 0 ]]; then
    INTERACTIVE=true
fi

# Allow override via environment or flag
if [[ "$1" == "--non-interactive" ]] || [[ "$RUFLO_NONINTERACTIVE" == "1" ]]; then
    INTERACTIVE=false
elif [[ "$1" == "--interactive" ]]; then
    INTERACTIVE=true
fi

echo "🚀 Ruflo Path A Installation"
echo "================================"
echo ""

# Check if Claude Code is available
if ! command -v claude &> /dev/null; then
    echo "❌ Claude Code CLI not found"
    echo "Please install Claude Code: https://claude.ai/code"
    exit 1
fi

echo "✅ Claude Code CLI detected"
echo ""

# Step 1: Add marketplace
echo "📦 Step 1: Adding Ruflo marketplace..."
claude plugin marketplace add ruvnet/ruflo
echo "✅ Marketplace added"
echo ""

# Step 2: Install core
echo "📦 Step 2: Installing ruflo-core..."
claude plugin install -y ruflo-core@ruflo
echo "✅ ruflo-core installed"
echo ""

# Step 3: Optional plugins
echo "📦 Step 3: Optional plugins"
echo ""

# Install swarm
INSTALL_SWARM=${RUFLO_INSTALL_SWARM:-"n"}
if [[ "$INTERACTIVE" == "true" ]]; then
    read -p "Install swarm coordination (ruflo-swarm)? [y/N]: " -n 1 -r
    echo
    INSTALL_SWARM="$REPLY"
fi

if [[ $INSTALL_SWARM =~ ^[Yy]$ ]]; then
    claude plugin install -y ruflo-swarm@ruflo
    echo "✅ ruflo-swarm installed"
fi
echo ""

# Install memory & RAG
INSTALL_RAG=${RUFLO_INSTALL_RAG:-"n"}
if [[ "$INTERACTIVE" == "true" ]]; then
    read -p "Install memory & RAG (ruflo-rag-memory)? [y/N]: " -n 1 -r
    echo
    INSTALL_RAG="$REPLY"
fi

if [[ $INSTALL_RAG =~ ^[Yy]$ ]]; then
    claude plugin install -y ruflo-rag-memory@ruflo
    echo "✅ ruflo-rag-memory installed"
fi
echo ""

# Install vector database
INSTALL_DB=${RUFLO_INSTALL_DB:-"n"}
if [[ "$INTERACTIVE" == "true" ]]; then
    read -p "Install vector database (ruflo-agentdb)? [y/N]: " -n 1 -r
    echo
    INSTALL_DB="$REPLY"
fi

if [[ $INSTALL_DB =~ ^[Yy]$ ]]; then
    claude plugin install -y ruflo-agentdb@ruflo
    echo "✅ ruflo-agentdb installed"
fi
echo ""

# Verification
echo "📋 Verifying installation..."
echo ""
claude plugin list | grep -i ruflo || echo "⚠️  No Ruflo plugins found"
echo ""

# Final steps
echo "================================"
echo "✅ Installation Complete!"
echo ""
echo "Next steps:"
echo "1. In Claude Code, run: /ruflo init"
echo "2. Check: /help ruflo"
echo "3. Explore: /ruflo status"
echo ""
echo "For full CLI (Path B), run:"
echo "  npx ruflo init --wizard"
echo ""

if [[ "$INTERACTIVE" == "false" ]]; then
    echo "ℹ️  Running in non-interactive mode"
    echo "To enable interactive prompts, use: $0 --interactive"
    echo "Or set optional plugins via environment variables:"
    echo "  RUFLO_INSTALL_SWARM=y RUFLO_INSTALL_RAG=y RUFLO_INSTALL_DB=y $0"
    echo ""
fi
