# -*- coding: utf-8 -*-
# @Time    :2019/4/3 5:49 PM
# @Author  : wangqiao


from . import celery


@celery.task
def test_task():
    return "test_task"


@celery.task
def test_task1():
    return "test_task1"
