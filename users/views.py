from django.shortcuts import render
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

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


class PaymentListAPIView(ListAPIView):
    """контроллер для списка платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ['pay_date']
