#wrappers
def input_clear_and_type(local_driver, locator, value):
    local_input = local_driver.find_element_by_id(locator)
    local_input.clear()
    local_input.send_keys(value)