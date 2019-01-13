from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address', views.AddressView)
router.register('client', views.ClientView)

urlpatterns = [
    path('', include(router.urls))
]