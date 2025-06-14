import pytest
from selenium import webdriver
from tracker import NovaPoshtaTracker

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_tracking_status(driver):
    tt_number = "59001380043792"  
    expected_status = "Отримана"   

    tracker = NovaPoshtaTracker(driver)
    actual_status = tracker.get_status(tt_number)

    assert expected_status in actual_status