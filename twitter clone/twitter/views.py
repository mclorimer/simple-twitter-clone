from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
User = get_user_model()


def get_user(request):
	return User.objects.get(id=request.session['user_id'])

class IndexView(LoginRequiredMixin, View):

	def get(self, request):

		return render(request, 'twitter/index.html')
