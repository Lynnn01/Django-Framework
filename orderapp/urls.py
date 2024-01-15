from django.urls import path
from orderapp import views

urlpatterns = [
    path("order", views.order)
]
