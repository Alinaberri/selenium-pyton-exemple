
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.group1020
def test_example():

    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)


    browser.get('https://www.apple.com/')
    print(browser.title)
    browser.find_element(By.LINK_TEXT, "Find a Store").click()
    print(browser.title)
    browser.find_element(By.CLASS_NAME, "form-textbox-input").send_keys("Roanoke" + Keys.ENTER)



