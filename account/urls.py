from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.Home, name='home'),
    path('logout/', views.Logout, name='logout'),
]