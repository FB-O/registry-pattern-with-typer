# A simple implementation of the `Registry` pattern in Python using `Typer`

A Python CLI project template built with [Typer](https://typer.tiangolo.com/), featuring auto-discovery of command groups and a central command registry.

## Structure

```
.
├── README.md
├── requirements.txt
├── setup.py
└── src
    └── cli_tool
        ├── __init__.py
        ├── cli.py              # Entry point, command loader, typer wiring
        ├── registry.py         # Central command registry 
        ├── commands
        │   ├── __init__.py
        │   ├── placeholder     # Example command group
        │   │   ├── __init__.py
        │   │   ├── goodbye.py  # Module `goodbye.py` with command function `goodbye()`
        │   │   └── hello.py    # Module `hello.py` with command function 'hello()`
        │   └── placeholder_2   # Additional command group placeholder
        │       └── __init__.py
        └── core 
            ├── config.py
            └── connection.py
```


## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

## Usage

```bash
cli-tool --help
cli-tool hello_world hello --message "hi"
cli-tool hello world goodbye --message "bye"
```

## Adding a command

1. Create a new package under `src/cli_tool/commands/your_group/`
2. Add an `__init__.py` and a module with your command function
3. Decorate it with `@register("your_group", "your_command")`

The command will be picked up automatically on next run — no wiring needed.
