import tomllib
from pathlib import Path

import pytest

from utils.afc import AFC
from utils.dut import DUT
from utils.rf import RF


def load_config(config_path: str) -> dict:
    """Load configuration from a TOML file."""
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Can't find config file: {config_path}")

    with open(config_file, "rb") as f:
        return tomllib.load(f)


def pytest_addoption(parser):
    """Add command line options"""
    parser.addoption(
        "--config",
        action="store",
        default="configs/test.toml",
        help="Path to the configuration file",
    )


@pytest.fixture(scope="session")
def config(request):
    """Global config fixture"""
    config_path = request.config.getoption("--config")
    return load_config(config_path)


@pytest.fixture
def dut(config):
    """DUT fixture"""
    dut_config = config.get("dut", {})
    dut = DUT(dut_config)
    yield dut


@pytest.fixture
def afc(config):
    """AFC fixture"""
    afc_config = config.get("afc", {})
    afc = AFC(api_url=afc_config.get("api_url"))
    yield afc


@pytest.fixture
def rf(config):
    """RF fixture"""
    rf_config = config.get("rf", {})
    rf = RF(api_url=rf_config.get("api_url"))
    yield rf


def pytest_sessionstart(session):
    """Create environment.properties file at the start of the session."""
    config_path = session.config.getoption("--config")
    config = load_config(config_path)
    with open("./reports/allure-results/environment.properties", "w") as f:
        f.write(f"DUT {config['dut']['host']}\n")
        f.write(f"AFC {config['afc']['api_url']}\n")
        f.write(f"RF {config['rf']['api_url']}\n")


def pytest_runtest_setup(item):
    print()
