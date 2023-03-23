import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)


browser.get('http://www.ebay.com/')
browser.find_element(By.LINK_TEXT, "Motors").click()


def wait_for_the_dropdown_and_select_value(time, name, value):
    dropdown = WebDriverWait(browser, timeout=time).until(EC.element_to_be_clickable((By.NAME, name)))
    Select(dropdown).select_by_visible_text(value)


wait_for_the_dropdown_and_select_value(5, "Year", "2020")
wait_for_the_dropdown_and_select_value(5, "Make", "BMW")
wait_for_the_dropdown_and_select_value(6, "Model", "X5")
wait_for_the_dropdown_and_select_value(6, "Trim", "M Sport Utility 4-Door")
wait_for_the_dropdown_and_select_value(4, "Engine", "4.4L 4395CC V8 GAS DOHC Turbocharged")
browser.find_element(By.CLASS_NAME, "motors-finder__find-btn").click()