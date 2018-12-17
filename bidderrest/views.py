from django.shortcuts import render
from rest_framework import viewsets
from bidder.models import Location
from .serializers import AddressSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = AddressSerializer

