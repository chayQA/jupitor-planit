import pytest
from pageObject.config.config_file import ConfigData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



@pytest.mark.usefixtures('init_driver')
class BaseTest:

    @pytest.fixture(scope='function')
    def init_driver(self, request):

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        request.cls.driver = web_driver
        yield
        web_driver.quit()

