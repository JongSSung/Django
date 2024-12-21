from django.urls import path
from . import views

urlpatterns = [
    path('Search_Web/', views.search_web, name='search_web'),
]