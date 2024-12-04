from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Jobs
from .serializers import JobSerializer

class JobListAPI(APIView):
    def get(self, request):
        jobs = Jobs.objects.all()  # QuerySet to fetch all jobs
        serializer = JobSerializer(jobs, many=True)  # Serialize QuerySet
        return Response(serializer.data)  # Return serialized data
