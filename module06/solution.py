import os
import platform
import pytest
import unittest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetWeather(unittest.TestCase):

    def setUp(self):
        self.driver_path = str(Path.cwd()).replace('\\','/') + '/drivers/Linux/chromedriver'
        self.driver = webdriver.Chrome(self.driver_path)

    def get_weather(self, days=5):
        self.weather_days = days
        self.driver.get('http://www.bbc.com/weather/727011')
        
        self.accept_privacy = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "bbcprivacy-continue-button")))
        self.accept_privacy.click()
        #self.accept_cookies = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, './/[@id="bbccookies-continue-button"]/span')))
        self.accept_cookies = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'bbccookies-continue-button')))
        self.accept_cookies.click()

        #self.list_of_day_parent_elements = [self.driver.find_element_by_id(f'daylink-{i}') for i in range(1, self.weather_days+1)]
        self.list_of_day_parent_elements = self.driver.find_element_by_id('daylink-1')
        self.list_of_childs_weather = self.list_of_day_parent_elements.find_element_by_class_name("wr-day__details__weather-type-description")
        self.toprint = self.list_of_childs_weather.text # Currently is empty, probably as I have to point the parent element first!?
        print(self.toprint)

    def tearDown(self):
        self.driver.quit()

weather = GetWeather()
weather.setUp()
weather.get_weather()
weather.tearDown()