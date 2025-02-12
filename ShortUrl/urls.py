from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.create_shortened_link),
    path('<str:code>/', views.redirect_shortened_link),
]
