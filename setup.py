# -*- coding: utf-8 -*-
# @Time    :2019/4/1 5:21 PM
# @Author  : wangqiao


from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'pytest',
        'coverage',
        'celery',
        'flask-celery-helper',  # Flask官网上的flask-celery包可能因为长期未维护的原因，在应用中与python的celery包存在兼容问题
        'redis'
    ],
)
