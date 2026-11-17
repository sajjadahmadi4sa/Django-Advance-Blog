import pytest
from django.urls import reverse
from datetime import datetime
from rest_framework.test import APIClient
from accounts.models import User, Profile
from blog.models import Category
from django.utils import timezone


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="admin@admin.com", password="sajjad1376")
    Profile.objects.create(
        user=user,
        first_name="test_first_name",
        last_name="test_last_name",
        description="test description",
    )
    return user


@pytest.fixture
def common_category():
    return Category.objects.create(name="test_category")


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api_v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(
        self, api_client, common_user, common_category
    ):
        url = reverse("blog:api_v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "category": common_category.name,
            "published_date": timezone.now(),
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("blog:api_v1:post-list")
        data = {"title": "test", "content": "description"}
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
