from django.test import TestCase
from django.shortcuts import render
# Create your tests here.
import requests



def testerhome_login():
    # data为请求入参
    datas = {
        'username': '13717888314',
        'password': '1q2w3e4r5t6y'
    }
    # data = {username=13717888314&password=1q2w3e4r5t6y}

    headers = {
        "Content-Type":"multipart/form-data"
    }
    url = "https://openwhy.net/api/auth/login"
    # 编码格式为application/x-www-form-urlencoded;charset=UTF-8，所以请求参数为dict，使用data参数
    r = requests.post(url,datas)
    res = r.text
    body = r.json()
    print("res:" + res)
    print("body:" + body)
    status_code = str(r.status_code)
    token = body["datas"]["token"]
    print("status_code:"+status_code)
    print("token:"+token)
    # return token,{'data':res}

def testappid():

    header = "X-Authorization:"
    url = "https://open.openwhy.net/api/v1/weapp/manager/apply/list"
    r = requests.get(url)
    res = r.text
    body = r.json()


if __name__ == '__main__':
    testerhome_login()
