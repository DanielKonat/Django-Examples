from django.conf.urls import url
from customer import views

urlpatterns = [
  #url(r'^$', views.index),
  url(r'^create/$', views.index),
  url(r'^prodlist/$', views.prodlist),
]