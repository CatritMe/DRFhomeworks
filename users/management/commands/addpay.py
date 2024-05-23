from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    """Команда для создания платежа"""
    def handle(self, *args, **options):
        payment = Payment.objects.create()
        #payment.course = Course.objects.get(pk=1)
        payment.lesson = Lesson.objects.get(pk=1)
        payment.save()