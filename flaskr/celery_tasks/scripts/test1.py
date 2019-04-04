# from ..celery_ob import celery
from flaskr import celery_ob

@celery_ob.task
def test_task1():
    return "test_task1"

