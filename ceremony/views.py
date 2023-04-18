from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ceremony, Participant


class CeremonyRegistrationView(LoginRequiredMixin, View):
    def get_ceremony(self, ceremony_id):
        return Ceremony.objects.get(id=ceremony_id)

    def get(self, request, ceremony_id):
        context = {'ceremony': self.get_ceremony(ceremony_id)}
        return render(request, 'ceremony_registration.html', context)

    def post(self, request, ceremony_id):
        ceremony = self.get_ceremony(ceremony_id)
        participant_name = request.POST.get('participant_name')
        if participant_name:
            Participant.objects.create(name=participant_name, ceremony=ceremony, user=request.user)
        return redirect('ceremony_detail', pk=ceremony.pk)