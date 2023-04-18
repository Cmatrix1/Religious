from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Event
from .serializers import EventSerializer


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        date_param = self.kwargs.get('date')
        if not date_param:
            date_param = datetime.today().strftime('%Y-%m-%d')

        return Event.objects.filter(date=date_param)