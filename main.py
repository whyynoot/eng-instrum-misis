from dotenv import load_dotenv
import os 
from yandex_oauth import YandexOAuthSelenium
from yandex_disk import YandexDisk


if __name__ == "__main__":
    load_dotenv()

    auth = YandexOAuthSelenium()
    token = auth.authenticate()

    disk = YandexDisk(token)
    disk.download_file(os.getenv("DISK_FILE_PATH"), os.getenv("DOWNLOAD_FILE_PATH"))