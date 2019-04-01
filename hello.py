# -*- coding: utf-8 -*-
# @Time    :2019/4/1 5:01 PM
# @Author  : wangqiao


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
