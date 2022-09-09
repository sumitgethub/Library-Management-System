from django.urls import path

from Book.views import BookApi



urlpatterns = [
    path('api/',BookApi.as_view()),
    path('api/<int:pk>/',BookApi.as_view()),

]