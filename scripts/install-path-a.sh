#!/bin/bash
# Ruflo Path A Installation Script
# Installs Ruflo plugins via Claude Code marketplace

set -e

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
claude plugin install ruflo-core@ruflo
echo "✅ ruflo-core installed"
echo ""

# Step 3: Offer optional plugins
echo "📦 Step 3: Optional plugins"
echo ""
echo "Install additional plugins? (y/n for each)"
echo ""

read -p "Install swarm coordination (ruflo-swarm)? [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    claude plugin install ruflo-swarm@ruflo
    echo "✅ ruflo-swarm installed"
fi
echo ""

read -p "Install memory & RAG (ruflo-rag-memory)? [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    claude plugin install ruflo-rag-memory@ruflo
    echo "✅ ruflo-rag-memory installed"
fi
echo ""

read -p "Install vector database (ruflo-agentdb)? [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    claude plugin install ruflo-agentdb@ruflo
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
