from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create$', views.CreateUserView.as_view(), name='create'),
	url(r'^login$', views.UserLoginView.as_view(), name='login'),
]
