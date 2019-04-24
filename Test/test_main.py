import pytest
import time

@pytest.mark.usefixtures("invoke_browser")
class Test_Main:

    @pytest.fixture(autouse=True)
    def initialSetup(self,invoke_browser):
        pass

    @pytest.mark.run(order=1)
    def test_open_url(self):
        driver = self.driver
        print(driver.title)

        time.sleep(2)