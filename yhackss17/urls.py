from django.urls import path

from . import views

urlpatterns = [
    path('/1/<str:text>/', views.text),
    path(r'/2/<str:url>', views.voice)
]
