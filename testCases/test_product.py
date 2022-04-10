import pytest
from selenium import webdriver
from pageObjects.ProductPage import ProductPage

class Test_001_Product:
    baseURL = "http://selenium1py.pythonanywhere.com/en-gb/"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title == "Oscar - Sandbox":
            assert True
        else:
            assert False

    def test_product(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.pd = ProductPage(self.driver)
        self.pd.clickAllProduct()
        self.driver.close()

    def test_addbasket(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.pd = ProductPage(self.driver)
        self.pd.clickAllProduct()
        self.pd.clickAddToBasket()
        self.driver.close()

    def test_viewbasket(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.pd = ProductPage(self.driver)
        self.pd.clickAllProduct()
        self.pd.clickAddToBasket()
        self.pd.clickViewBasket()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Basket | Oscar - Sandbox":
            assert True
        else:
            assert False

    def test_checkout(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.pd = ProductPage(self.driver)
        self.pd.clickAllProduct()
        self.pd.clickAddToBasket()
        self.pd.clickViewBasket()
        self.pd.clickcheckout()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Basket | Oscar - Sandbox":
            assert True
        else:
            assert False