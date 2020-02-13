from django.views.generic import ListView
from django.shortcuts import render


class ProfileSite(ListView):
    template_name = "user_profile.html"
    name = 'profile-site'

    def get(self, request):
        """
        This function was abandoned but left for future
        :param request:
        :return:
        """
        return render(request, self.template_name, {'form': ''})
