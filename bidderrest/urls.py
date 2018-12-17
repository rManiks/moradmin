from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address', views.AddressView)

urlpatterns = [
    path('', include(router.urls))
]