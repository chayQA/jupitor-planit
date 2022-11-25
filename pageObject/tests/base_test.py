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
        web_driver = webdriver.Chrome(executable_path=ConfigData.CHROME_DRIVER_PATH, options=options)
        request.cls.driver = web_driver
        yield
        web_driver.quit()

