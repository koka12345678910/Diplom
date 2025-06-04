from celery import shared_task

@shared_task
def send_notification(manga_id):
    print(f"[Celery] Уведомление: у манги с ID {manga_id} новая глава!")
    return True
