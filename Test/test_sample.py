import pytest
import time

@pytest.mark.usefixtures("invoke_browser")
class Test_URL:

    def test_open_url(self):
        driver = self.driver
        print(driver.title)

        time.sleep(2)