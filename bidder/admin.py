from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Location)
admin.site.register(Client)
admin.site.register(ServiceProvier)
admin.site.register(BookingRequest)
admin.site.register(Bid)