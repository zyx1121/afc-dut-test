import json
from pathlib import Path

import requests

from utils.logger import logger


class AFC:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def set_test_vector(self, test_vector: str) -> bool:
        url = f"{self.api_url}/setTestVector"
        response = requests.post(url, params={"test_vector": test_vector})

        if response.status_code == 200:
            logger.info(f"Successfully set test vector: {test_vector}")
            return True
        else:
            logger.error(f"Failed to set test vector: {response.json().get('detail')}")
            return False

    def get_last_request(self) -> dict:
        url = f"{self.api_url}/getLastRequest"
        response = requests.get(url)
        return response.json()
