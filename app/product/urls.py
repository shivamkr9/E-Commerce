from django.urls import path, include
from product import views
from rest_framework import routers

app_name = "product"
router = routers.DefaultRouter()
router.register("category", views.CatoegoryView, basename="category")
router.register("item", views.ProductView, basename="item")


urlpatterns = [
    path("", include(router.urls)),
]
