from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from users.forms import UserLoginForm

User = get_user_model()
# Create your views here.
def logout_view(request):
    logout(request)

    return redirect("users:index")

class IndexView(View):
	
	def get(self, request):
		return render(request, 'users/index.html')
		

class CreateUserView(View):
	form_class = UserCreationForm
	
	def get(self, request):
		context = {
			'user_creation_form': self.form_class()
		}
		return render(request, 'users/create.html', context)
		
		
	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			#User.objects.create(**form.cleaned_data)
			user = form.save()
			login(request, user)
			return redirect(settings.LOGIN_SUCCESS_PAGE)
		else:
			context = {
				'user_creation_form': form
			}
			return render(request, 'users/create.html', context)

class UserLoginView(View):

    form_class = AuthenticationForm

    def get(self, request):
        context = {
            'user_login_form': self.form_class()
        }
        return render(request, 'users/login.html', context)
        
        
    def post(self, request):
        form = self.form_class(request=request, data=request.POST)
        error = "YA DUN GOOFED. CONTACTING THE CYBER POLICE."
        

        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_SUCCESS_PAGE)
        context = {
            'user_login_form': form
        }
        return render(request, 'users/login.html', context)