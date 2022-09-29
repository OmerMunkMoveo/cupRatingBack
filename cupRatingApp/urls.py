from django.urls import path
from . import views

urlpatterns = [
    path('cups/', views.cups, name='cups'),
]