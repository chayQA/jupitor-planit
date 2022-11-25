import time
from pageObject.pages.base_page import BasePage
from pageObject.config.config_xlsx import ConfigXlsxData
from pageObject.config.config_file import ConfigData
from selenium.webdriver.common.by import By


class ShopPage(BasePage):
    SHOP_PAGE_BUTTON = (By.XPATH, '//a[normalize-space()="Shop"]')
    STUFFTED_FROG_BUY_BUTTON = (By.XPATH, '//h4[normalize-space()="Stuffed Frog"]/..//a')
    FLUFFY_BUNNY_BUY_BUTTON = (By.XPATH, '//h4[normalize-space()="Fluffy Bunny"]/..//a')
    VALENTINE_BEAR_BUY_BUTTON = (By.XPATH, '//h4[normalize-space()="Valentine Bear"]/..//a')
    CART_BUTTON = (By.XPATH, '//a[contains(text(), "Cart")]')
    TOYS_IN_CART = (By.XPATH, '//table[@class="table table-striped cart-items"]//tbody//tr')
    TOTAL_SUM = (By.XPATH, '//tfoot//td/strong')
    SUBTOTAL = (By.XPATH, '//table[@class="table table-striped cart-items"]//tbody//td[4]')
    STUFFTED_FROG_PRICE = (By.XPATH, '//h4[normalize-space()="Stuffed Frog"]/..//span')
    FLUFFY_BUNNY_PRICE = (By.XPATH, '//h4[normalize-space()="Fluffy Bunny"]/..//span')
    VALENTINE_BEAR_PRICE = (By.XPATH, '//h4[normalize-space()="Valentine Bear"]/..//span')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.JUPITER_HOME_URL)

    def do_click_shop_button(self):
        self.do_click(self.SHOP_PAGE_BUTTON)
        time.sleep(3)
    
    def do_buy_toy_stuffed_frog(self, quantity):
        for i in range(quantity):
            self.do_click(self.STUFFTED_FROG_BUY_BUTTON)
            time.sleep(2)

    def do_buy_toy_fluffy_bunny(self, quantity):
        for i in range(quantity):
            self.do_click(self.FLUFFY_BUNNY_BUY_BUTTON)
            time.sleep(2)

    def do_buy_toy_valentine_bear(self, quantity):
        for i in range(quantity):
            self.do_click(self.VALENTINE_BEAR_BUY_BUTTON)
            time.sleep(2)
    
    def do_click_cart(self):
        self.do_click(self.CART_BUTTON)

    def get_sub_total(self):
        all_items = self.find_elements_by_xpath(self.SUBTOTAL)
        return [float(each.text.replace('$', '')) for each in all_items]
        
    def calucalte_sub_total(self, number_of_toys): 


        sub_total = []
        one_toy_price = []
        for each in range(1, len(number_of_toys)+1):

            price_xpath = (By.XPATH, self.TOYS_IN_CART[1]+f'[{each}]//td[2]')
            price = float(self.get_element_text(price_xpath).replace('$',''))
            count_xpath = (By.XPATH, self.TOYS_IN_CART[1]+f'[{each}]//td[3]//input')
            count = int(self.find_element_by_xpath(count_xpath).get_attribute('value'))
            one_toy_price.append(price)
            sub_total.append(price*count)
        return sub_total,one_toy_price

    


    def get_total_sum(self):
        return float(self.get_element_text(self.TOTAL_SUM).split(':')[1])

    def get_price_stuffted_frog(self):
        
        return float(self.get_element_text(self.STUFFTED_FROG_PRICE).replace('$',''))
  
    def get_price_fluffy_bunny(self):
        return float(self.get_element_text(self.FLUFFY_BUNNY_PRICE).replace('$',''))
  
    def get_price_valentine_bear(self):
        return float(self.get_element_text(self.VALENTINE_BEAR_PRICE).replace('$',''))



    
