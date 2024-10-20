from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductModelViewSet, basename='products')
router.register('categories', views.CategoryModelViewSet, basename='categories')
urlpatterns = router.urls
