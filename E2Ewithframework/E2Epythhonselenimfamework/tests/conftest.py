
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# it's a command line hook to parse
from selenium.webdriver.support.wait import WebDriverWait


driver=None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setUp(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if(browser_name=="chrome"):
        option=webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--ignore-certificate-errors")
        serive_obj=Service("C:\\chromedriver.exe")
        driver=webdriver.Chrome(service=serive_obj,options=option)
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/angularpractice/")

        # i'm not returning this driver object to the required function bcz if i return the yield(teardown) will not execute else viceversa
        # so plz assign the driver to the calling class attribute that's the particulat calling class attribute(global var for all objects)
        request.cls.driver=driver
        yield
        driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

