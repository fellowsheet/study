from django.urls import path, include
from .views import APIAuthor

urlpatterns = [
    path('authors/', APIAuthor.as_view()),
    path('authors/<int:pk>/', APIAuthor.as_view()),
    path('accounts/', include(('accounts.urls', 'accounts'))),
]
