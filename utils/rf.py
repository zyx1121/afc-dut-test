from utils.logger import logger


class RF:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def start_monitoring(self) -> bool:
        # TODO: Start RF monitoring
        logger.info("Start RF monitoring")
        return True

    def check_status(self) -> bool:
        # TODO: Check RF status
        logger.info("Check RF status")
        return True
