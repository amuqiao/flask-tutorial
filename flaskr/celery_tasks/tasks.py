# coding:utf-8

from celery import Celery
from datetime import timedelta


def make_celery(app):
    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379',  # Broker 地址
        CELERY_RESULT_BACKEND='redis://localhost:6379',  # 结果存储地址
        # 定时任务，
        CELERYBEAT_SCHEDULE={
            'task3': {
                'task': 'flaskr.celery_tasks.scripts.test1.test_task1',
                'schedule': timedelta(seconds=5),
                "args": '',
            },
            'task4': {
                'task': 'flaskr.celery_tasks.scripts.test2.test_task2',
                "schedule": timedelta(seconds=10),
                "args": '',
            },
        },
        CELERY_TASK_PATH=[
            'flaskr.celery_tasks.scripts.test1',
            'flaskr.celery_tasks.scripts.test2']
    )
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        include=app.config['CELERY_TASK_PATH'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


# 创建celery应用对象
# celery = make_celery(app)

# 导入celery的配置信息
# celery_ob.config_from_object("celery_tasks.config")

"""启动"""

# celery -A celery_tasks.celery_ob.py worker -l info  -B
# celery -A celery_tasks.celery_ob.py worker -l info  -B
# celery -A celery_ob worker -l info  -B
