import os

from selenium import webdriver
from pyshadow.main import Shadow
from concurrent import futures
from dotenv import load_dotenv

from src.credentials import Credential
from src.procedures import login, go_to_RU

options = webdriver.FirefoxOptions()
options.add_argument("--headless=new")

load_dotenv()

if (os.getenv('CREDENTIALS_FILE_LOCATION') == None):
    print('Credentials File is not defined')
    exit()

print('Get credentials')
credentials = Credential(
    os.getenv('CREDENTIALS_FILE_LOCATION')).getCredentials()


def buy_ru_process(credential):
    navigator = webdriver.Firefox(options=options)
    shadow = Shadow(navigator)

    navigator.get('https://auth.unesp.br/login?')

    login(navigator, credential)
    go_to_RU(navigator)


with futures.ThreadPoolExecutor() as executor:
    """
    Generate a concurrence web drivers for each credential in parallel
    """
    for credential in credentials:
        executor.submit(buy_ru_process, credential)
