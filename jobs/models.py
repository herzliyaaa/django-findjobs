from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self)  -> str:
        return self.title
    
    class Meta:
        verbose_name = "Job"  # Singular name
        verbose_name_plural = "Jobs"  # Correct plural name