from django.urls import path

from . import views

urlpatterns = [
    path('/<int:type>/<str:text>/', views.text)
]
