import requests


class YandexDisk:
    def __init__(self, access_token):

        self.api_base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {
            'Authorization': f'OAuth {access_token}',
            'Accept': 'application/json'
        }

    def get_download_link(self, file_path):
        try:
            response = requests.get(f"{self.api_base_url}/resources/download?path=disk:/{file_path}", headers=self.headers)

            if response.status_code == 200:
                download_url = response.json().get('href')
                print(f"Download URL: {download_url}")
                return download_url
            else:
                raise Exception(f"Failed to get download link: {response.status_code} {response.text}")
        except Exception as e:
            raise e

    def download_file(self, file_path, save_as):
        try:
            download_url = self.get_download_link(file_path)
            file_response = requests.get(download_url)

            if file_response.status_code == 200:
                with open(save_as, "wb") as file:
                    file.write(file_response.content)
                print(f"File downloaded successfully as {save_as}!")
            else:
                raise Exception(f"Failed to download file: {file_response.status_code} {file_response.text}")
        except Exception as e:
            raise e