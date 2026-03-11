import importlib
import logging
import pkgutil

import typer

from cli_tool.registry import get_registry

logging.basicConfig(
        format = "%(asctime)s %(levelname)-8s %(message)s", 
        level = logging.INFO, 
        )
app = typer.Typer()


def load_commands() -> None:
    import cli_tool.commands
    for finder, name, ispkg in pkgutil.iter_modules(cli_tool.commands.__path__):
        if not ispkg: 
            continue
        logging.info(f"Found command group:\t{name}")
        package_name = f"cli_tool.commands.{name}"
        package = importlib.import_module(package_name)

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            logging.info(f"Loading command @\t{package_name}.{module_name}")
            importlib.import_module(f"{package_name}.{module_name}")

def register_with_typer() -> None:
    for group, commands in get_registry().items():
        group_app = typer.Typer()
        app.add_typer(group_app, name=group)
        for name, func in commands:
            group_app.command(name)(func)


def main() -> None:
    load_commands()
    register_with_typer()
    app()

if __name__ == '__main__':
    main()
