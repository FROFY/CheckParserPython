import requests
import config

url = config.url
token = config.token


def OrderWithStr(qr_string):
    data = {
        'token': token,
        'qrraw': qr_string
    }
    response = requests.post(url=url, data=data)
    items = response.json()
    item = items["data"]["json"]["items"][0]["name"]
    price = items["data"]["json"]["items"][0]["price"] / 100
    count = items["data"]["json"]["items"][0]["quantity"]
    return item, price, count


def OrderWithPhoto():
    data = {
        'token': token
    }
    files = {
        'qrfile': open(r"C:\Users\Kukushkin_IA\Downloads\receipt.jpg", 'rb')
    }
    response = requests.post(url=url, data=data, files=files)
    return response.json()
