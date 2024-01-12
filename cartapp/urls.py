from cartapp import views
from django.urls import path

urlpatterns = [
    path("cart", views.cart),
    path("cart/add/<int:product_id>", views.addCart, name="addCart"),
]
