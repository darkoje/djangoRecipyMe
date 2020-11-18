from django.conf.urls import url
from . import views

app_name= 'accounts'

urlpatterns = [
    url(r'^$', views.view_profile, name="profiles"),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_the_profile'),
]






