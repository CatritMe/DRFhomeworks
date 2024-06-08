from django.core.management import BaseCommand

from materials.models import Lesson
from users.models import Payment


class Command(BaseCommand):
    """Команда для создания платежа"""
    def handle(self, *args, **options):
        payment = Payment.objects.create()
        payment.lesson = Lesson.objects.get(pk=1)
        payment.save()
