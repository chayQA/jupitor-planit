from email import message_from_string
from pageObject.pages.base_page import BasePage
from pageObject.config.config_xlsx import ConfigXlsxData
from pageObject.config.config_file import ConfigData
from selenium.webdriver.common.by import By


class ContactPage(BasePage):
    CONTACT_BUTTON = (By.XPATH, '//a[normalize-space()="Contact"]')
    SUBMIT_BUTTON = (By.XPATH, '//a[normalize-space()="Submit"]')
    ERROR_MESSAGES = (By.XPATH, '//span[@class="help-inline ng-scope"]')
    FORE_NAME_INPUT = (By.XPATH, '//input[@name="forename"]')
    SURNAME_INPUT = (By.XPATH, '//input[@name="surname"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    TELEPHONE_INPUT = (By.XPATH, '//input[@name="telephone"]')
    MESSAGE_TEXT_INPUT =(By.XPATH, '//textarea[@name="message"]')
    FORM_SUBMIT_SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alert alert-success"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.JUPITER_HOME_URL)

    def do_click_contact_buttton(self):
        self.do_click(self.CONTACT_BUTTON)

    def do_click_submit_button(self):
        self.do_click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        elements = self.find_elements_by_xpath(self.ERROR_MESSAGES)
        text = [each.text for each in elements]
        return text

    def fill_form_with_data(self, username):
        self.do_send_keys(self.FORE_NAME_INPUT, username)
        self.do_send_keys(self.SURNAME_INPUT, 'USERSURNAME')
        self.do_send_keys(self.EMAIL_INPUT, 'user@mail.com')
        self.do_send_keys(self.TELEPHONE_INPUT, '02 1234 5678')
        self.do_send_keys(self.MESSAGE_TEXT_INPUT, 'Sample message')


    def get_form_success_message(self):
        return self.get_element_text(self.FORM_SUBMIT_SUCCESS_MESSAGE)
