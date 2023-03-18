import pytest
from pageObject.config.config_file import ConfigData
from selenium import webdriver

@pytest.mark.usefixtures('init_driver')
class BaseTest:

    @pytest.fixture(scope='function')
    def init_driver(self, request):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.binary_location

        web_driver = webdriver.Chrome(options =options) 
        request.cls.driver = web_driver
        yield
        web_driver.quit()

