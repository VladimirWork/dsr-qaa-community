import pytest
from selenium import webdriver
import locators
import lib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()


@pytest.fixture(scope="class")
def driver_setup():
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    print(driver.title)
    assert 'Selenium' in driver.title

    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.ID, "at-cv-lightbox-close"))).click()
    """"""
    yield
    """"""
    driver.quit()


@pytest.mark.usefixtures('driver_setup')
class TestForm:

    @pytest.mark.parametrize(
        'value_a, value_b, output',
        [
            (1, 1, "2"),
            (0, -1, "-1"),
            ("a", "b", "NaN"),
            (1, 3, "4")
        ]
    )
    def test_output(self, value_a, value_b, output):
        lib.input_clear_and_type(driver, locators.sum_page["input_a_id"], value_a)
        lib.input_clear_and_type(driver, locators.sum_page["input_b_id"], value_b)

        get_total_button = driver.find_element_by_xpath(locators.sum_page["get_total_button_xpath"])
        get_total_button.click()

        actual_output = driver.find_element_by_id(locators.sum_page["actual_output_id"]).text

        assert output == actual_output
