from celery import task

@task
def celery_task_console_log_num(num):
    print(f'------> CELERY task, console log: {num}')
    return True