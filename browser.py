from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import time

from settings import DRIVER_LOCATION, URL_CREATE, TIME_WAIT

def create_workspace(email):

    def submit_code(code):
        input_fields = browser.find_elements_by_class_name('inline_input')
        for input_field, digit in zip(input_fields, code):
            input_field.clear()
            input_field.send_keys(digit)
            time.sleep(0.25)

    browser = webdriver.Chrome(executable_path=DRIVER_LOCATION)
    browser.get(URL_CREATE)
    try:
        sign_up_id = 'signup_email'
        email_input = WebDriverWait(browser, TIME_WAIT).until(expected_conditions
                                                              .presence_of_element_located((By.ID, sign_up_id)))
        email_input.clear()
        email_input.send_keys(email)
    except TimeoutException as error:
        pass
    submit_button = WebDriverWait(browser, TIME_WAIT).until(expected_conditions.element_to_be_clickable((By.ID, 'submit_btn')))
    submit_button.click()
    WebDriverWait(browser, TIME_WAIT).until(expected_conditions
                                            .presence_of_element_located((By.CLASS_NAME, 'confirmation_code_group')))

    # TODO: request to mailgun for code
    submit_code('123456')
    time.sleep(5)
    company_name = WebDriverWait(browser, TIME_WAIT).until(expected_conditions
                                            .presence_of_element_located((By.ID, 'signup_team_name')))
    company_name.clear()
    submit_button = WebDriverWait(browser, TIME_WAIT).until(
        expected_conditions.element_to_be_clickable((By.ID, 'submit_btn')))
    submit_button.click()


if __name__ == '__main__':
    create_workspace('ibragim1989@gmail.com')

