from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class ProfileView(View):
    def get(self, request):
        # user = request.user
        # if not user.is_authenticated:
        #     return HttpResponse(status=401)
        return render(request, 'profile.html')
