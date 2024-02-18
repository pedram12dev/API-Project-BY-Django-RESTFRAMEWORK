"""
Test for the tags api
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Tag
from recipe.serializers import TagSerializer

TAGS_URL = reverse('recipe:tag-list')


def create_user(email='user@example.com', password='testpass123'):
    """create and return a user"""
    return get_user_model().objects.create_user(email=email, password=password)


class PublicTagsApiTest(TestCase):
    """Test unauthenticated API request"""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """test auth is required for retrieving tags"""
        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code , status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTest(TestCase):
    """test authenticated api request"""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """test retrieving a list of tags"""
        Tag.objects.create(user=self.user , name='pedram')
        Tag.objects.create(user=self.user , name='fatima')
        res = self.client.get(TAGS_URL)
        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags , many=True)
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        self.assertEqual(res.data , serializer.data)

    def test_tags_limited_to_user(self):
        """test list of tags is limited to authenticated user"""
        user2 = create_user(email='test2@example.com')
        Tag.objects.create(user=user2, name='peyman')
        tag = Tag.objects.create(user=self.user , name='saman')

        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'],tag.name )
        self.assertEqual(res.data[0]['id'], tag.id)




