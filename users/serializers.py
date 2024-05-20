from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    """сериалайзер для платежей"""
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    """сериалайзер для пользователей"""
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")


class UserDetailSerializer(ModelSerializer):
    """расширенный сериалайзер для пользователей"""
    payment = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = "__all__"
