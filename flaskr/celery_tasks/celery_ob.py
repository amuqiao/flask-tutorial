# coding:utf-8
# from __future__ import absolute_import # 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
from celery import Celery
# from flaskr import app
from celery import Celery


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
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
