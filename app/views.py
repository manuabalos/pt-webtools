from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import SurveyResponse
from .serializers import SurveyResponseSerializer
from rest_framework.permissions import IsAuthenticated

class SurveyResponseListView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        responses = SurveyResponse.objects.all().order_by('id')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(responses, request)
        serializer = SurveyResponseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = SurveyResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SurveyResponseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return SurveyResponse.objects.get(pk=pk)
        except SurveyResponse.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        response = self.get_object(pk)
        serializer = SurveyResponseSerializer(response)
        return Response(serializer.data)