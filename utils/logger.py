import sys
from pathlib import Path

from loguru import logger

try:
    import allure

    class AllureLogHandler:
        def write(self, message):
            allure.attach(message.strip(), "Log", allure.attachment_type.TEXT)

    logger.add(AllureLogHandler(), format="{message}", level="DEBUG")

except ImportError:
    pass
