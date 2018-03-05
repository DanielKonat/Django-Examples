from django.conf.urls import url
from student import views
urlpatterns=[
 url(r'^add/$',views.add),
 url(r'^studlist/$',views.studlist), 
 ]