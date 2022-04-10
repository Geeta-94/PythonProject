class ProductPage:
    button_product_xpath="//*[@id='browse']/li/ul/li[1]/a"
    button_addtobasket_xpath="//*[@id='default']/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button"
    button_viewbasket_xpath="//*[@id='messages']/div[3]/div/p[2]/a[1]"
    button_proceedtocheckout_xpath="//*[@id='content_inner']/div[3]/div/div/a"

    def __init__(self,driver):
        self.driver=driver

    def clickAllProduct(self):
            self.driver.find_element_by_xpath(self.button_product_xpath).click()

    def clickAddToBasket(self):
            self.driver.find_element_by_xpath(self.button_addtobasket_xpath).click()

    def clickViewBasket(self):
            self.driver.find_element_by_xpath(self.button_viewbasket_xpath).click()

    def clickcheckout(self):
            self.driver.find_element_by_xpath(self.button_proceedtocheckout_xpath).click()