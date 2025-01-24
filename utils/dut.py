import time
from typing import Dict

import paramiko

from utils.logger import logger


class DUTControlError(Exception):
    """DUT Control Error"""

    pass


class DUT:
    def __init__(self, config: dict):
        self._connected: bool = False
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self._load_config(config)

    def _load_config(self, config: dict):
        """Load config"""
        dut_config = config.get("connection", {})

        self._host = dut_config.get("host", "192.168.1.1")
        self._port = dut_config.get("port", 22)
        self._username = dut_config.get("username", "admin")
        self._password = dut_config.get("password", "password")

        self._retry_count = dut_config.get("retry_count", 3)
        self._retry_delay = dut_config.get("retry_delay", 5)

        self._connect_timeout = dut_config.get("connect_timeout", 10)
        self._command_timeout = dut_config.get("command_timeout", 30)

    def connect(self) -> bool:
        """Connect to DUT device, including retry mechanism"""
        for attempt in range(self._retry_count):
            try:
                if attempt > 0:
                    logger.warning(f"Retry connecting to DUT (第 {attempt + 1} 次)")
                    time.sleep(self._retry_delay)

                self._client.connect(
                    hostname=self._host,
                    username=self._username,
                    password=self._password,
                    port=self._port,
                    timeout=self._connect_timeout,
                )

                self._connected = True
                logger.info("Successfully connected to DUT")
                return True

            except paramiko.AuthenticationException as e:
                logger.error(f"DUT authentication failed: {str(e)}")
                raise DUTControlError(
                    "Authentication failed, please check authentication information"
                )

            except (paramiko.SSHException, TimeoutError) as e:
                logger.error(
                    f"DUT connection failed (attempt {attempt + 1}/{self._retry_count}): {str(e)}"
                )
                if attempt == self._retry_count - 1:
                    raise DUTControlError(
                        f"Connection failed, tried {self._retry_count} times"
                    )
                continue

    def shell(self, cmd: str) -> Dict:
        """Execute DUT command and return actual execution result"""
        if not self._connected:
            self.connect()

        try:
            logger.debug(f"Executing command: {cmd}")

            stdin, stdout, stderr = self._client.exec_command(
                cmd, timeout=self._command_timeout
            )

            exit_code = stdout.channel.recv_exit_status()

            return {
                "code": exit_code,
                "stdout": stdout.read().decode("utf-8"),
                "stderr": stderr.read().decode("utf-8"),
            }

        except Exception as e:
            logger.error(f"Command {cmd} failed: {str(e)}")

            if isinstance(e, (paramiko.SSHException, EOFError)):
                self._connected = False
                self._client = paramiko.SSHClient()
                self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                return self.shell(cmd)  # Retry executing command

            return {"code": 1, "stdout": "", "stderr": str(e)}

    def setup(self) -> bool:
        """
        The AFC DUT is required to configure its Radio to use the maximum DUT power capability
        that complies with maximum permissible EIRP/PSD provided by the AFC DUT Test harness.
        Optionally, AFC DUT may have a test regulatory identifier (e.g., FCC ID),
        geographic coordinates, antenna height, and uncertainty, etc.
        to initiate an Available Spectrum Inquiry Request when triggered from AFC DUT Test Harness.
        The AFC DUT is required to configure only one chain active and turn off all remaining chains.
        """
        # TODO: Implement DUT initialization logic
        logger.info("Setup DUT")
        return True

    def send_available_spectrum_inquiry_request(self):
        """Send frequency inquiry request"""
        # TODO: Implement frequency inquiry logic
        logger.info("Let DUT send frequency inquiry request")
        return True

    def __del__(self):
        """Clean up resources"""
        if self._connected:
            try:
                self._client.close()
            except:
                logger.warning("Close SSH connection failed")
