from django.urls import path
from .views import JobListAPI, JobDetailAPI, JobCategoriesListAPI

urlpatterns = [
    path('jobs/', JobListAPI.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailAPI.as_view(), name='job-detail'),
    path('job-categories/', JobCategoriesListAPI.as_view(), name='job-category-list')
]