import logging
from cli_tool.registry import register


@register("hello_world", "hello")
def hello_world(
        message: str = ''
        ) -> None:
    logging.info(f"group: 'hello', name: 'world', message: '{message}'.")
