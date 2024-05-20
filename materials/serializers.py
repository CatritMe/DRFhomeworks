from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """сериалайзер для урока"""
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """сериалайзер для курса"""
    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lessons_count(obj):
        """возвращает lessons_count - количество уроков в курсе"""
        return Lesson.objects.filter(course=obj.pk).count()

    def get_lessons(self, obj):
        """возвращает lessons - все уроки в курсе"""
        return [lesson.title for lesson in Lesson.objects.filter(course=obj.pk)]
