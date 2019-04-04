# from ..celery_ob import celery
from flaskr import celery_ob


@celery_ob.task
def test_task2():
    return "test_task2"

