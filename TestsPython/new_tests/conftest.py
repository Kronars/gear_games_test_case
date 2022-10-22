import pytest
from altunityrunner import AltUnityDriver
from altunityrunner import logger

@pytest.fixture(scope="module")
def driver_conn():
    altdriver = AltUnityDriver(timeout=5)
    logger.disable("altunityrunner")
    yield altdriver
    altdriver.stop()

@pytest.fixture()
def scene_main(driver_conn):
    driver_conn.load_scene('Main')
    driver_conn.wait_for_current_scene_to_be('Main', 3)

@pytest.fixture()
def scene_shop(driver_conn):
    driver_conn.load_scene('Shop')
    driver_conn.wait_for_current_scene_to_be('Shop', 3)
