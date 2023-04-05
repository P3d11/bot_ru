from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


def login(navigator, credential):
    """
    navigator: selenium.webdriver.firefox.webdriver.WebDriver
    credential: {user: str, password: str}
    """

    user, password = credential['user'], credential['password']
    time.sleep(1)

    # user
    parent = navigator.find_element(
        'xpath', '/html/body/md-content/div[1]/div/form/md-card/md-input-container[1]')
    list_child = parent.find_elements(By.CLASS_NAME, 'md-input')
    list_child[0].send_keys(user)

    # password
    parent = navigator.find_element(
        'xpath', '/html/body/md-content/div[1]/div/form/md-card/md-input-container[2]')
    list_child = parent.find_elements(By.CLASS_NAME, 'md-input')
    list_child[0].send_keys(password)

    navigator.find_element(
        'xpath', '/html/body/md-content/div[1]/div/form/md-card/button').click()

    print('\nlogged')


def go_to_RU(navigator):
    time.sleep(4)

    try:
        navigator.find_element(
            'xpath', '/html/body/div[2]/div/md-content/div[2]/md-list/md-list-item[@href="https://sistemas.unesp.br/ru-bauru"]/div/a').click()
    except:
        print('failed')

    try:
        WebDriverWait(navigator, 10).until(EC.element_to_be_clickable(
            ('xpath', '/html/body/div[2]/div[1]/div/ul/li[2]/a')))
    except TimeoutException:
        print('the page failed to load')

    navigator.find_element(
        'xpath', '/html/body/div[2]/div[1]/div/ul/li[2]/a').click()
