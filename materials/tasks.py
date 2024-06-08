import datetime
from datetime import timedelta, datetime
import pytz

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Course, Subscription
from users.models import User

"""		
1. celery -A config worker -P eventlet -l info
2. celery -A config.celery beat -l info
"""


@shared_task
def send_email(course_id):
    """функция отправки письма для подписчиков курса"""
    course = Course.objects.get(pk=course_id)
    subscribers = Subscription.objects.get(course=course_id)

    send_mail(
        subject=f'Курс {course} обновлен',
        message=f'Курс {course},на который вы подписаны обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscribers.user.email]
    )


@shared_task
def check_activity():
    """блокировка неактивных пользователей"""
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)
    active_users = User.objects.filter(is_active=True)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user} заблокирован из-за длительного отсутствия")
