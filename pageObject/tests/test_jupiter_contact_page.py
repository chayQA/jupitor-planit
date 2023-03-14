import pytest
from pageObject.pages.jupiter_contact_page import ContactPage
from pageObject.tests.base_test import BaseTest
from pageObject.config.config_xlsx import ConfigXlsxData
from pageObject.config.config_file import ConfigData


class TestContactPage(BaseTest):

    def go_to_contact_page(self):
        self.contact_page = ContactPage(self.driver)
        self.contact_page.do_click_contact_buttton()
        assert self.contact_page.get_current_page_url() == ConfigData.JUPITER_CONTACT_PAGE_URL

    def test_submit_without_input(self):
        self.go_to_contact_page()
        self.contact_page.do_click_submit_button()
        assert self.contact_page.get_error_message() == ['Forename is required', 'Email is required', 'Message is required']

    @pytest.mark.repeat(5)
    def test_submit_with_input(self):
        username = 'USER'
        self.go_to_contact_page()
        self.contact_page.fill_form_with_data(username)
        self.contact_page.do_click_submit_button()
        success_message =  "Thanks {}, we appreciate your feedback.".format(username)
        assert self.contact_page.get_form_success_message() == success_message
    

