from __future__ import unicode_literals

from django.db import models


class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    street = models.CharField(max_length=100, blank=True, default='')
    province = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    postal_code = models.CharField(max_length=50, blank=True, default='')
    apartment = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=50, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.name


class Party(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='party', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    venue = models.ForeignKey(Venue, related_name='party', on_delete=models.CASCADE)
    description = models.TextField(default='')
    party_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.name


class GuestList(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='guestlist', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    party = models.ForeignKey(Party, related_name='guestlist', on_delete=models.CASCADE)
    number_of_guests = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.name
