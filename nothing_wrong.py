from selenium import webdriver
from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from getpass import getpass
import time
import os

user = ''
password = ''

def set_login():
    global user
    global password
    
    user = input('user: ')
    password = getpass('password: ')
    
    os.system('clear')
    
    print('login set')

def login():    
    time.sleep(1)
    
    #user
    parent = nav.find_element('xpath', '/html/body/md-content/div[1]/div/form/md-card/md-input-container[1]')
    list_child = parent.find_elements(By.CLASS_NAME, 'md-input')
    list_child[0].send_keys(user)
    
    #password
    parent = nav.find_element('xpath', '/html/body/md-content/div[1]/div/form/md-card/md-input-container[2]')
    list_child = parent.find_elements(By.CLASS_NAME, 'md-input')
    list_child[0].send_keys(password)
    
    nav.find_element('xpath', '/html/body/md-content/div[1]/div/form/md-card/button').click()
    
    print('\nlogged')
    
def go_to_RU():
    """     try:
        WebDriverWait(nav, 10).until(EC.element_to_be_clickable(('xpath', '/html/body/div[2]/md-sidenav/md-content/md-menu-content/md-menu-item[1]/button')))
    except TimeoutException:
        print('the page failed to load') """
    
    time.sleep(4)
    
    try:
        nav.find_element('xpath', '/html/body/div[2]/div/md-content/div[2]/md-list/md-list-item[3]/div/a').click()
    except:
        print('failed')
        
    try:
        WebDriverWait(nav, 10).until(EC.element_to_be_clickable(('xpath', '/html/body/div[2]/div[1]/div/ul/li[2]/a')))
    except TimeoutException:
        print('the page failed to load') 
        
    nav.find_element('xpath', '/html/body/div[2]/div[1]/div/ul/li[2]/a').click()


os.system('clear')


set_login()


options = webdriver.FirefoxOptions()
options.add_argument("--headless=new")

nav = webdriver.Firefox(options = options)
shadow = Shadow(nav)
nav.get('https://auth.unesp.br/login?')


login()


go_to_RU()