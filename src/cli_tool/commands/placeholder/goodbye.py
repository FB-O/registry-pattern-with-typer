import logging
from cli_tool.registry import register


@register("hello_world", "goodbye")
def hello_world(
        message: str = ''
        ) -> None:
    logging.info(f"group: 'goodbye', name: 'world', message: '{message}'.")

