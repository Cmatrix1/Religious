
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Poll, PollOptions


class PollListView(ListView):
    model = Poll
    template_name = 'poll_list.html'
    context_object_name = 'polls'


class PollCreateView(CreateView):
    model = Poll
    pk_url_kwarg = 'id'
    fields = ['question', 'active']
    template_name = 'poll_create.html'
    success_url = reverse_lazy('poll_list')

    def form_valid(self, form):
        self.object = form.save()
        options_texts = self.request.POST.getlist('option')
        if options_texts:
            for text in options_texts:
                if text.strip():
                    poll_option = PollOptions(poll=self.object, option=text)
                    poll_option.save()
        return super().form_valid(form)



class PollVoteView(APIView):
    def get(self, request, pk, option_pk):
        poll = Poll.objects.filter(pk=pk).first()
        poll_option = PollOptions.objects.filter(poll=poll, pk=option_pk).first()
        user = request.user
        if user in poll_option.voters.all():
            poll_option.voters.remove(user)
            return Response({'message': 'Vote removed successfully.'}, status=status.HTTP_400_BAD_REQUEST)

        poll_option.voters.add(user)
        poll_option.save()
        return Response({'message': 'Vote added successfully.'}, status=status.HTTP_200_OK)



class PollResultView(DetailView):
    model = Poll
    template_name = 'poll/poll_result.html'
    context_object_name = 'poll'