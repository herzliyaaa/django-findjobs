from django.urls import path
from .views import JobListAPI

urlpatterns = [
    path('api/jobs/', JobListAPI.as_view(), name='job-list'),  # API endpoint
]