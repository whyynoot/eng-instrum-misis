from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from dotenv import load_dotenv
import os

load_dotenv()

class YandexOAuthSelenium:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.redirect_uri = "https://oauth.yandex.ru/verification_code"
        self.access_token = None

    def authenticate(self):
        oauth_url = (
            f"https://oauth.yandex.ru/authorize?"
            f"response_type=token&client_id={self.client_id}"
        )

        driver = webdriver.Chrome()

        try:
            print("Opening browser for Yandex OAuth...")
            driver.get(oauth_url)

            for _ in range(3):
                WebDriverWait(driver, 120).until(EC.url_contains(self.redirect_uri)) 

                current_url = driver.current_url
                token_match = re.search(r'[#&]access_token=([^&]+)', current_url)
                if token_match:
                    self.access_token = token_match.group(1)
                    print(f"Access token obtained: {self.access_token}")
                    return self.access_token
                else:
                    print("Access token not found in URL.")
        finally:
            driver.quit()

        return self.access_token