from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(ModelViewSet):
    """контроллер для CRUD курса"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """Проверка прав доступа модератора"""
        if self.action == 'create':
            self.permission_classes = (~IsModerator, IsAuthenticated,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner,)
        elif self.action in ['update', 'list', 'retrieve']:
            self.permission_classes = (IsAuthenticated, IsModerator | IsOwner,)
        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    """контроллер для создания урока"""
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModerator,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """контроллер для просмотра списка уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    """контроллер для просмотра одного урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonUpdateAPIView(UpdateAPIView):
    """контроллер для редактирования урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonDestroyAPIView(DestroyAPIView):
    """контроллер для удаления урока"""
    queryset = Lesson.objects.all()
    permission_classes = (IsOwner,)
