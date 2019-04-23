import pytest
import pytest_html
from selenium import webdriver
from time import sleep
from Driver.webdriver_factory import GetWebdriverInstance

# Send request variable to the fixture
## Browser value will be set from request.config.getoption (from command prompt)
@pytest.yield_fixture(scope="class")
def invoke_browser(request, browser):
    wdf = GetWebdriverInstance(browser)
    driver = wdf.getbrowserInstance()

    # Set class attribute and assign the variable
    if request.cls is not None:
        driver.get("https://chain.unionbankph.com/i2i/home")
        driver.maximize_window()
        request.cls.driver = driver
    yield driver
    driver.quit()

# Create 2 parsers to get value from command prompt
def pytest_addoption(parser):
    parser.addoption("--browser")

#Return the argument value
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")



#Fixture for Firefox
# @pytest.fixture(params=["chrome", "firefox"],scope="class")
# def driver_init(request):
#     if request.param == "chrome":
#         path = 'D:\\chromedriver.exe'
#         driver = webdriver.Chrome(executable_path=path)
        
#     if request.param == "firefox":
#         path = 'D:\\geckodriver.exe'
#         driver = webdriver.Firefox(executable_path=path)

#     driver.get("https://chain.unionbankph.com/i2i/home")
#     driver.maximize_window()
#     request.cls.driver = driver

#     yield driver

#     driver.close()