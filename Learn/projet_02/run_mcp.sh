#!/bin/bash
# Wrapper pour lancer le serveur MCP avec le bon PYTHONPATH
export PYTHONPATH="/home/felix/Desktop/Exegol/OFFICIALMCPREPO/Leanr_Python_MCP/venv/lib/python3.12/site-packages:$PYTHONPATH"
exec /usr/bin/python3.12 "$(dirname "$0")/solution.py" "$@"
