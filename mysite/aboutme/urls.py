from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^education', views.education, name='education'),
    url(r'^work', views.work, name='work'),
    url(r'^contract', views.work, name='contract'),
]