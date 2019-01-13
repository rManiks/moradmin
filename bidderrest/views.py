from django.shortcuts import render
from rest_framework import viewsets
from bidder.models import Location, Client
from .serializers import AddressSerializer, ClientSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = AddressSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer