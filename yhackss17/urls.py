from django.urls import path

from . import views

urlpatterns = [
    path('/1/<str:text>/', views.text),
    path('/2/<str:text>/', views.voice)
]
