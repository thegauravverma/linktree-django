from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("login",views.login_request, name='login'),
    path("logout",views.logout_request,name='logout'),
    path("<str:name>", views.showlinks, name="link")
]
