from asyncio.log import logger
from dataclasses import dataclass

from flask import Flask,request
from flask_cors import CORS
import requests
import json
import pymysql
db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='chat'
)

host = ""
post = "post"
url = ''.join([host,post])
data = {
    'message':,
    're_chat':,
    'stream':
}

app = Flask(__name__)
CORS(app)


# 定义headers
headers = {
    'accept': 'application/json',
    'AUTHORIZATION': 'application-xxxxxxxxxxxxxxxxxxx'  # api key
}

# 获取 profile id
def get_profile_id():
    profile_url = 'http://localhost:8888/api/application/profile'  # 自己的url
    response = requests.get(profile_url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['id']
    else:
        print("获取profile id失败")
        return None

# 获取 chat id
def get_chat_id(profile_id):
    chat_open_url = f'http://localhost:8888/api/application/{profile_id}/chat/open'  # 改为自己的url
    response = requests.get(chat_open_url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print("获取chat id失败")
        return None



@app.route('/')
def index():
    return 'Hello Flask!!!'
@app.route('/api/help')
def help():
    print("help()")
    return 'need data'
@app.route('/api/user/login',methods={'POST'})
def userLogin():
    if request.data:
        res = request.data.decode('utf-8')
        print(res)
        return '获取成功'
    else :
        return '没有数据'

@app.route('/api/chat/send',methods={'POST'})
def send():
    if request.data:
        res = request.data.decode('utf-8')
        data = {
            'message':res.join(),
            're_chat':False,
            'stream':False,
        }
        ans = requests.post(url,data)
        return



if __name__ == "__main__":
    app.run(debug=True)
    # debug==True是为了方便修改代码之后，能够不重启项目就能够更新，否则，每次更改代码都需要重新启动项目
    # 其他参数的设置可以查阅文档，这里越简单越好