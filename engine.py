import requests;

url = 'http://mail.ru';

num = requests.get(url);

print(num.text)

class Engine:
    """Base class"""
    apiUrl = "https://api-metrika.yandex.net/stat/v1/data"

    def get(self):
        pass

        