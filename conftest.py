import pytest
from selenium import webdriver
from configuration import config as path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

driver = None
#driver_path = ("C:\\chromedriver.exe")
imdb_url = "https://www.imdb.com/search/name/"

@pytest.fixture(scope="class")
def chrome_driver(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(imdb_url)
    request.cls.driver = imdb_url

    yield driver
    # Teardown Chrome driver
    driver.quit()

