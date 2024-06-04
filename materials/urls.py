from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, SubscriptionCreateAPIView

from materials.views import LessonUpdateAPIView, LessonRetrieveAPIView, LessonListAPIView, LessonCreateAPIView, LessonDestroyAPIView

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet,)

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_view'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/destroy/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscribe'),
]

urlpatterns += router.urls
