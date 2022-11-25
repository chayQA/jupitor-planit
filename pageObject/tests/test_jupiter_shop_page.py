import pytest
from pageObject.pages.jupiter_shop_page import ShopPage
from pageObject.tests.base_test import BaseTest
from pageObject.config.config_xlsx import ConfigXlsxData
from pageObject.config.config_file import ConfigData


class TestShopPage(BaseTest):

    def go_to_shop_page(self):
        self.shop_page = ShopPage(self.driver)
        self.shop_page.do_click_shop_button()
        assert self.shop_page.get_current_page_url() == ConfigData.JUPITER_SHOP_PAGE_URL

    def test_order_toys(self):
       """
       test case to verify subtotal and total in the cart page
       """
       self.go_to_shop_page()
       toys_numbers = [2,5,3]
       toy_price_shop_page = [
           self.shop_page.get_price_stuffted_frog(),
           self.shop_page.get_price_fluffy_bunny(),
           self.shop_page.get_price_valentine_bear()
       ]
       self.shop_page.do_buy_toy_stuffed_frog(toys_numbers[0])
       self.shop_page.do_buy_toy_fluffy_bunny(toys_numbers[1])
       self.shop_page.do_buy_toy_valentine_bear(toys_numbers[2])
       self.shop_page.do_click_cart()
       caluclated_sub_total = self.shop_page.calucalte_sub_total(toys_numbers)[0]
       toy_price_cart_page = self.shop_page.calucalte_sub_total(toys_numbers)[1]
       assert toy_price_shop_page == toy_price_cart_page
       assert self.shop_page.get_sub_total() == caluclated_sub_total
       assert self.shop_page.get_total_sum() == sum(caluclated_sub_total)

        

