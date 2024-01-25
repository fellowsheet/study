from django.urls import path, include
from . import views

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
