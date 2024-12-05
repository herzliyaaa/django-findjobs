from rest_framework import serializers
from .models import Jobs

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['id', 'title', 'created_on', 'posted_by'] 
        read_only_fields = ['id', 'created_on'] 