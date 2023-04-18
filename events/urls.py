from django.urls import path
from .views import EventListAPIView

urlpatterns = [
    path('events/<str:date>/', EventListAPIView.as_view(), name='event-list'),
]