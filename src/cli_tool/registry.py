from typing import Callable


# { group_name: [(command_name, callable), ...]}
_registry: dict[str, list[tuple[str, Callable]]] = {}


def register(group: str, name: str) -> Callable:
    """
    Register a function as a CLI command under the given group.

    Args:
        group:  The CLI group this command belongs to (e.g. "hello_world_commands", "other_commands").
        name:   The name of the command as it will appear in the CLI.

    Returns:
        A decorator that registers the fnctio nand returns it unchanged.
    """
    def decorator(func: Callable) -> Callable:
        _registry.setdefault(group, []).append((name, func))
        return func
    return decorator


def get_registry() -> dict[str, list[tuple[str, Callable]]]:
    """Return the full registry."""
    return _registry
