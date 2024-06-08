from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class LessonSerializer(ModelSerializer):
    """сериалайзер для урока"""
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


def get_lessons(obj):
    """возвращает lessons - все уроки в курсе"""
    return [lesson.title for lesson in Lesson.objects.filter(course=obj.pk)]


class CourseSerializer(ModelSerializer):
    """сериалайзер для курса"""
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()
    subscription = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lessons_count(obj):
        """возвращает lessons_count - количество уроков в курсе"""
        return Lesson.objects.filter(course=obj.pk).count()

    def get_subscription(self, obj):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return obj.subscription_set.filter(user=user).exists()


class SubscriptionSerializer(ModelSerializer):
    """Сериалайзер для подписок"""

    class Meta:
        model = Subscription
        fields = "__all__"
