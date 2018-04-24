from django.conf.urls import url

from . import views

app_name = 'liveapp'
urlpatterns = [
    
    url(r'^$', views.server_login, name='server_login'),
	url(r'^firstindex$', views.firstindex, name='firstindex'),
    url(r'^firstindex/secondindex$', views.secondindex, name='secondindex'),
  

]
    
    








