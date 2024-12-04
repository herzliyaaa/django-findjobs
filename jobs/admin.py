from django.contrib import admin
from .models import Jobs
# Register your models here.


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'created_on', 'last_modified')
    search_fields = ('title', 'posted_by__username')