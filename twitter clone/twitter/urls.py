from django.conf.urls import url
from twitter import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
]
