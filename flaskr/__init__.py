# -*- coding: utf-8 -*-
# @Time    :2019/4/1 5:14 PM
# @Author  : wangqiao

from celery.schedules import crontab
from datetime import timedelta
import os
from flask import Flask
from celery import Celery


def make_celery(app):
    # celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'], include=['flaskr.celery_tasks.scripts'])
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'], include=app.config['CELERY_TASK_PATH'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # # celery ====
    # app.config.update(
    #     CELERY_BROKER_URL='redis://localhost:6379',
    #     CELERY_RESULT_BACKEND='redis://localhost:6379'
    # )
    # celery = make_celery(app)
    #
    # @celery.task
    # def add_together(a, b):
    #     return a + b
    #
    # # celery ====
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello/')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)  # 在工厂中 导入和注册蓝图
    # 关联端点名称 'index' 和 / URL ，这样 url_for('index') 或 url_for('blog.index') 都会有效，会生成同样的 / URL
    app.add_url_rule('/', endpoint='index')

    return app


app = create_app()

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',  # Broker 地址
    CELERY_RESULT_BACKEND='redis://localhost:6379',  # 结果存储地址
    # 定时任务，
    CELERYBEAT_SCHEDULE={
        # 'task1': {
        #     'task': 'flaskr.tasks.test_task',
        #     # "schedule": timedelta(seconds=5),
        #     'schedule': timedelta(seconds=5),
        #     "args": '',
        # },
        # 'task2': {
        #     'task': 'flaskr.tasks.test_task1',
        #     "schedule": timedelta(seconds=10),
        #     "args": '',
        # },
        'task3': {
            'task': 'flaskr.celery_tasks.scripts.test1.test_task1',
            # "schedule": timedelta(seconds=5),
            'schedule': timedelta(seconds=5),
            "args": '',
        },
        'task4': {
            'task': 'flaskr.celery_tasks.scripts.test2.test_task2',
            "schedule": timedelta(seconds=10),
            "args": '',
        },
    },
    CELERY_TASK_PATH=['flaskr.celery_tasks.scripts.test1', 'flaskr.celery_tasks.scripts.test2']
)


celery_ob = make_celery(app)
# # 导入celery的配置信息
# celery.config_from_object("celery_tasks.config")


if __name__ == '__main__':
    # 启动celery
    """celery -A flaskr.celery_ob worker -l info  -B"""
    pass
