#!/bin/bash
# MCP Learning IDE Launcher
# Quick script to launch the interactive MCP learning environment

cd "$(dirname "$0")"

echo "🚀 Starting MCP Learning IDE..."
echo ""

# Check if rich is installed
python3 -c "import rich" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing required dependencies..."
    pip3 install rich
    echo ""
fi

# Launch the IDE
python3 mcp_ide.py

echo ""
echo "👋 Thanks for using MCP Learning IDE!"
