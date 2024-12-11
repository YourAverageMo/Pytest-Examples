from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Amazon:

    driver = ''

    def setup_method(self):
        chrome_driver_path = "./chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(
            options=options,
            service=Service(executable_path=chrome_driver_path))

    def amazon_search_pets(self):
        self.driver.get(
            "https://www.amazon.com/Best-Sellers-Pet-Supplies/zgbs/pet-supplies/ref=zg_bs_nav_pet-supplies_0"
        )

        items = self.driver.find_elements(By.ID, "gridItemRoot")

        for item in items:
            try:
                title_element = item.find_element(
                    By.CLASS_NAME, "_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
                print(title_element.text, '\n')
            except Exception as e:
                print(f"Error fetching title: {e}")

    def teardown_method(self):
        self.driver.close()


clicker = Amazon()

clicker.setup_method()
clicker.amazon_search_pets()
clicker.teardown_method()
