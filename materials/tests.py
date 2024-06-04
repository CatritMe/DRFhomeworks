from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@ad.com', password='admin')
        self.course = Course.objects.create(title='test', owner=self.user)
        self.lesson = Lesson.objects.create(title='test_les', course=self.course, url='url', owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_create(self):
        url = reverse('materials:course-list')
        data = {
            'title': 'test course',
            'description': 'descr test'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        data = {
            'title': 'test course new',
            'description': 'descr test'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'test course new'
        )

    def test_course_list(self):
        url = reverse('materials:course-list')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {'count': 1, 'next': None, 'previous': None, 'results': [{'id': self.course.pk, 'lessons_count': 1, 'lessons': ['test_les'], 'subscription': True, 'title': 'test', 'preview': None, 'description': None, 'owner': self.user.pk}]}
        )

    def test_course_delete(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_subscription(self):
        url = reverse('materials:subscribe')
        data = {
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json().get('message'), 'подписка удалена'
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@ad.com', password='admin')
        self.course = Course.objects.create(title='test', owner=self.user)
        self.lesson = Lesson.objects.create(title='test_les', course=self.course, url='url', owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_view', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'test_les'
        )

    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {
            'title': 'lesson_test',
            'course': self.course.pk,
            'url': 'https://www.youtube.com/watch?v=SuJCgGhN_SU',
            'owner': self.user.pk
        }
        data1 = {
            'title': 'lesson_test',
            'course': self.course.pk,
            'url': 'https://www.video.com/watch?v=SuJCgGhN_SU',
            'owner': self.user.pk
        }
        response = self.client.post(url, data)
        response1 = self.client.post(url, data1)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )
        self.assertEqual(
            response1.status_code, status.HTTP_400_BAD_REQUEST
        )

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            'title': 'lesson_test_new',
            'course': self.course.pk,
            'url': 'https://www.youtube.com/watch?v=SuJCgGhN_SU',
            'owner': self.user.pk
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'lesson_test_new'
        )

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {'count': 1, 'next': None, 'previous': None, 'results': [{'id': self.lesson.pk, 'title': 'test_les', 'preview': None, 'description': None, 'url': 'url', 'course': self.lesson.course.pk, 'owner': self.user.pk}]}
        )

    def test_lesson_delete(self):
        url = reverse('materials:lesson_destroy', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )
