from django.urls import path
from .views import SurveyResponseListView, SurveyResponseDetailView

urlpatterns = [
    path('responses/', SurveyResponseListView.as_view(), name='response-list'),
    path('responses/<int:pk>/', SurveyResponseDetailView.as_view(), name='response-detail'),
]