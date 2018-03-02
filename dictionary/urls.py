from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.words_list, name='words_list')
]