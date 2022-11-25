from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        """
        driver: mandidate argument the selenium driver object.
        """
        self.driver = driver
        self.driver.maximize_window()

    def do_click(self, by_locator):
        """
        by_locator: tuple with By class varible and locator
        returns: None, performs click operations on the located element if element is 
                        clickable.
        """
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """
        by_locator: tuple with By class varible and locator
        returns: None, Performs input to the text input located.
        """
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def find_element_by_xpath(self, by_locator):
        """
        by_locator: tuple with By class varible and locator
        returns: located element with the locator.
        """
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator))

    def find_elements_by_xpath(self, by_locator):
        """
        by_locator: tuple with By class varible and locator
        returns: located element with the locator.
        """
        return WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(by_locator))

    def clear_text(self, by_locator):
        """
        by_locator: tuple with By class varible and locator
        returns: None, clears the text from the located input field.
        """
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator)).clear()

    def get_element_text(self, by_locator):
        """
        by_locator: tuple with By class varible and locator
        return: text from the located element if found else return None
        """
        try:
            text = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locator)).text
            return text
        except:
            return None

    def get_title(self):
        """
        by_locator: tuple with By class varible and locator
        return: returns the title of the page.
        """
        return self.driver.title

    def is_visible(self, by_locator):
        """
        by_locator: tuple with By class varible and locator
        return: True if the element is visible else False
        """
        try:
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def go_back(self):
        """
        by_locator: tuple with By class varible and locator
        return: None, Perform the back navigation operation in the page.
        """
        self.driver.back()

    def go_forward(self):
        """
        by_locator: tuple with By class varible and locator
        return: None, Perform the forward navigation operation in the page.
        """
        self.driver.forward()

    def do_refresh(self):
        """
        by_locator: tuple with By class varible and locator
        return: None, Perform the page refresh operation in the page.
        """
        self.driver.refresh()

    def get_current_page_url(self):
        """
        by_locator: tuple with By class varible and locator
        return: current page url.
        """
        return self.driver.current_url