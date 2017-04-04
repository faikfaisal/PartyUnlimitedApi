from django.contrib import admin

from guestlist.models import Venue, Party, GuestList


admin.site.register(Venue)
admin.site.register(Party)
admin.site.register(GuestList)
