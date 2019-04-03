# -*- coding: utf-8 -*-
# @Time    :2019/4/3 10:37 AM
# @Author  : wangqiao


from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    print("{}".format(response.data))
    assert response.data == b'Hello, World!'
    # assert response.data == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected automatically to target URL: <a href="http://localhost/hello/">http://localhost/hello/</a>.  If not click the link.'

