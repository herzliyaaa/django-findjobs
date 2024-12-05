from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Jobs
from .serializers import JobSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class JobListAPI(APIView):
    @swagger_auto_schema(
        operation_description="Get the list of all jobs",
        tags=["Jobs"],
        responses={
            200: JobSerializer(many=True)
        },
    )
    def get(self, request):
        jobs = Jobs.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new job",
        operation_id="Create a job",
        tags=["Jobs"],
        request_body=JobSerializer,
        responses={
            "201": openapi.Response(
                description="Created",
                examples={
                    "application/json": {
                        "status": "success",
                        "message": "Account created successfully.",
                        "data": {
                            "title": "Developer",
                            "posted_by": 1,
                        },
                    }
                },
            )
        },
    )
    def post(self, request, format="json"):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            resp = {
                "status": "success",
                "data": {"message": "Account created successfully."},
            }

            return Response(resp, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPI(APIView):
    @swagger_auto_schema(
        operation_description="Get details of a specific job by ID",
        tags=["Jobs"],
        responses={200: JobSerializer},
    )
    def get(self, request, pk):
        try:
            job = Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            return Response(
                {"error": "Job not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = JobSerializer(job)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update the details of a specific job by ID",
        tags=["Jobs"],
        request_body=JobSerializer,
        responses={200: JobSerializer},
    )
    def put(self, request, pk):
        try:
            job = Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            return Response(
                {"error": "Job not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update the details of a specific job by ID",
        tags=["Jobs"],
        request_body=JobSerializer,
        responses={200: JobSerializer},
    )
    def patch(self, request, pk):
        try:
            job = Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            return Response(
                {"error": "Job not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific job by ID",
        tags=["Jobs"],
        responses={204: "No content"},
    )
    def delete(self, request, pk):
        try:
            job = Jobs.objects.get(pk=pk)
        except Jobs.DoesNotExist:
            return Response(
                {"error": "Job not found."}, status=status.HTTP_404_NOT_FOUND
            )

        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
