import requests
from bs4 import BeautifulSoup
import requests as req
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

webbrowser.open('http://10.100.211.150/deloedu_test/CoreHost/auth/login', new=2)

# Инициализируем браузер
def auth_request(username, password):
    response = requests.post("http://10.100.211.150/deloedu_test/CoreHost/auth/login", data={
    "username": username,
    "password": password
    })
    return response


username = "Елисеев"
password = "Qwerty1234"
response = auth_request(username, password)

