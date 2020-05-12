from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import locators
from lib import *


def check_output(local_driver, value_a, value_b, output):
    input_clear_and_type(local_driver, locators.sum_page["input_a_id"], value_a)
    input_clear_and_type(local_driver, locators.sum_page["input_b_id"], value_b)

    get_total_button = local_driver.find_element_by_xpath(locators.sum_page["get_total_button_xpath"])
    get_total_button.click()

    actual_output = local_driver.find_element_by_id(locators.sum_page["actual_output_id"]).text

    result = "Failure"
    if output == actual_output:
        result = "Success"

    print(f"Check: {value_a} + {value_b} = {actual_output} - {result}")


def main():
    driver = webdriver.Firefox()
    try:
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        print(driver.title)
        assert 'Selenium' in driver.title
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sum_page["close_button"]))).\
            click()
        with open('data.csv') as data_csv:
            reader = csv.reader(data_csv)
            headers = next(reader, None)
            for row in reader:
                check_output(driver, row[0], row[1], row[2])
    finally:
        driver.quit()


if __name__ == "__main__":
    main()