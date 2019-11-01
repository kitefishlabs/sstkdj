from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView

from .forms import EmailUserCreationForm
from .models import EmailUser


from django.contrib.auth.models import Group
from rest_framework import viewsets
from .serializers import EmailUserSerializer, GroupSerializer


class EmailUserViewSet(viewsets.ModelViewSet):
    queryset = EmailUser.objects.all().order_by('-date_joined')
    serializer_class = EmailUserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RegistrationView(CreateView):
    form_class = EmailUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'


# def dashboard(request):
#     try:
#         user = BifCoinUser.objects.get(proposal_email=request.user.email)
#     except BifCoinUser.DoesNotExist:
#         user = BifCoinUser(user=request.user, proposal_email=request.user.email,
#                            balance=0, pending_balance=0, state='claimed')
#     linked_email = ''
#     claimable = False
#     claimed = False
#     proposals = []

#     if (user is not None):
#         linked_email = user.proposal_email
#         if (user.state == 'claimed'):
#             claimed = True
#         else:
#             claimable = True

#         proposals = ClaimedProposal.objects.filter(
#             proposal_email=user.proposal_email).order_by('proposal_datetime')

#     return render(request, 'user/dashboard.html', {'claimable': claimable, 'claimed': claimed, 'linked_email': linked_email, 'linked_proposals': list(proposals), 'bifuser': user})
