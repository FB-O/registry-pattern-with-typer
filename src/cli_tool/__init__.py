# expose `main` since `./setup.py` uses `cli_tool:main`

from cli_tool.cli import main

__all__ = ["main"]
