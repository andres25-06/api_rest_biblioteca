from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("autores", views.AutorViewSet)
router.register("libros", views.LibroViewSet)
router.register("prestamos", views.PrestamoViewSet, basename="prestamo")

urlpatterns = [
    path("api/", include(router.urls)),
]
