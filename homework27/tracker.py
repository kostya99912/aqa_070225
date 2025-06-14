from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NovaPoshtaTracker:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def get_status(self, tt_number: str) -> str:
        # Open the tracking page
        self.driver.get(self.url)

        # Wait for the input field to appear and enter the tracking number
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "en"))
        )
        input_box.clear()
        input_box.send_keys(tt_number)

        # Wait until the search button becomes enabled (not disabled)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.ID, "np-number-input-desktop-btn-search-en").is_enabled()
        )

        # Click the search button
        search_button = self.driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
        search_button.click()

        # Wait for the status text to appear and return its text
        status_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
        )

        return status_element.text.strip()