from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """модель курса"""
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='materials/preview/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """модель урока"""
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='materials/preview/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    url = models.CharField(max_length=100, verbose_name='ссылка на урок')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
