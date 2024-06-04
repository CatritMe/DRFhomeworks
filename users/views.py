from django.shortcuts import render
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer, UserDetailSerializer


class UserViewSet(ModelViewSet):
    """вьюсет для модели пользователя"""
    queryset = User.objects.all()

    def get_serializer_class(self):
        """выбор сериалайзера для действия retrieve - конкретный пользователь"""
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer

    def perform_create(self, serializer):
        """При создании пользователя хэшировать пароль"""
        user = serializer.save(is_active=True)
        user.set_password(str(user.password))
        user.save()

    def get_permissions(self):
        """Проверка прав доступа"""
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class PaymentListAPIView(ListAPIView):
    """контроллер для списка платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ['pay_date']

