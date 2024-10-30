from asyncio.log import logger
from dataclasses import dataclass

from flask import Flask,request
from flask_cors import CORS

import pymysql
db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='chat'
)

app = Flask(__name__)
CORS(app)

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
        return '获取成功'


if __name__ == "__main__":
    app.run(debug=True)
    # debug==True是为了方便修改代码之后，能够不重启项目就能够更新，否则，每次更改代码都需要重新启动项目
    # 其他参数的设置可以查阅文档，这里越简单越好