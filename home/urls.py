from django.conf.urls import url

from django.contrib.auth.views import LoginView,LogoutView

from . import views

app_name='home'
urlpatterns=[
    url(r'^$',views.allnotes,name='all_notes'),
]
