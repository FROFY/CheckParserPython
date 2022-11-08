import requests

url = 'https://proverkacheka.com/api/v1/check/get'
token = '17229.R0nyP64mqKF7EaTHZ'


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
    # print('Товар: ' + item)
    # print('Цена: ' + str(price) + 'р')
    # print('Количество: ' + str(count))
