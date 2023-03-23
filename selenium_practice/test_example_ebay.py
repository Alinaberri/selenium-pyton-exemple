import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.group1020
def test_example():
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)


    browser.get('http://www.ebay.com/')
    browser.find_element(By.LINK_TEXT, "Motors").click()
    year_dropdown = WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable((By.NAME, "Year")))
    year = Select(year_dropdown).select_by_visible_text("2020")
    make_dropdown = WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable((By.NAME, "Make")))
    make = Select(make_dropdown).select_by_visible_text("BMW")
    model_dropdown = WebDriverWait(browser, timeout=5).until(EC.element_to_be_clickable((By.NAME, "Model")))
    model = Select(model_dropdown).select_by_visible_text("X5")
    trim_dropdown = WebDriverWait(browser, timeout=6).until(EC.element_to_be_clickable((By.NAME, "Trim")))
    trim = Select(trim_dropdown).select_by_visible_text("M Sport Utility 4-Door")
    engine_dropdown = WebDriverWait(browser, timeout=4).until(EC.element_to_be_clickable((By.NAME, "Engine")))
    engine = Select(engine_dropdown).select_by_value("4.4L 4395CC V8 GAS DOHC Turbocharged")
    browser.find_element(By.CLASS_NAME, "motors-finder__find-btn").click()