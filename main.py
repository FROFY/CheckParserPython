# -*- coding: utf-8 -*-

import json

import requests

from Deserialize import Root


def print_hi(qr_string):
    url = 'https://proverkacheka.com/api/v1/check/get'
    data = {
        'token': '17229.R0nyP64mqKF7EaTHZ',
        'qrraw': qr_string
    }
    response = requests.post(url=url, data=data)
    item = response.json()["data"]["json"]["items"][0]["name"]
    price = response.json()["data"]["json"]["items"][0]["price"] / 100
    print('Товар: ' + item)
    print('Цена: ' + str(price))


if __name__ == '__main__':
    print_hi('t=20221102T1352&s=89.99&fn=9960440301834413&i=6073&fp=1929603051&n=1')
