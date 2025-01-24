from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, default="No description available")
    status = models.CharField(max_length=10)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job Category"
        verbose_name_plural = "Job Categories"


class Jobs(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20)
    workplace_type = models.CharField(max_length=20)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
