from rest_framework import serializers
from .models import Jobs, JobCategory


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ["id", "title", "created_on", "posted_by"]
        read_only_fields = ["id", "created_on"]


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ["name", "description", "posted_by", "created_on"]
        read_only_fields = ["id", "created_on"]
