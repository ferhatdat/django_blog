
from django.urls import path, include
from rest_framework import routers
from .views import CategoryMVS, PostMVS

router = routers.DefaultRouter()
router.register('category', CategoryMVS)
router.register('post', PostMVS)

urlpatterns = [
    path('', include(router.urls)),
]