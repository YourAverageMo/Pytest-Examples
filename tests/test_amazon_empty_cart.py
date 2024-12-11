from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestAmazonCart:

    driver = ''

    def setup_method(self):
        chrome_driver_path = "./chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(
            options=options,
            service=Service(executable_path=chrome_driver_path))

    # TODO test failing because of amazon captcha
    # fixed. just changed link to anything but homepage. guess it looks like someone is just sharing a link with me so amazon doesnt want to interrupt
    def test_empty_cart(self):
        self.driver.get(
            "https://www.amazon.com/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2"
        )

        self.driver.find_element(By.ID, 'nav-cart').click()
        actual_text = self.driver.find_element(
            By.XPATH, "//div[@id='sc-active-cart']//h3").text
        expected_text = "Your Amazon Cart is empty"

        assert expected_text == actual_text, f"Error. Expected text: ({expected_text}), but actual text: ({actual_text})"

    def teardown_method(self):
        self.driver.close()
