from rest_framework import serializers
from bidder.models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('number', 'address_line_one', 'address_line_two', 'city', 'district', 'state', 'post_code', 'country')

  