from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import pytest


#Creating a class
class ViewTheVideo(unittest.TestCase):
    #creating a method/function
    def setUp(self):
        self.driver=webdriver.Chrome() #define the driver
        self.driver.maximize_window()
        self.driver.get("https://www.youtube.com/watch?v=MPfQZHDkm7c")
        sleep(3)
    def testViewVideo(self):
        coockie_accept_btn=self.driver.find_element(By.XPATH, "//button[@aria-label='Accept the use of cookies and other data for the purposes described']")
        coockie_accept_btn.click()
        sleep(33)
    def tearDown(self):
        self.driver.quit()