from django.contrib import admin
from .models import Jobs, JobCategory


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ("title", "posted_by", "created_on", "last_modified")
    search_fields = ("title",)
  


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "posted_by", "created_on", "last_modified")
    search_fields = ("name",)
