from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    apartment = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Party(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='party', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    venue = models.ForeignKey(Venue, related_name='party', on_delete=models.CASCADE)
    description = models.TextField(default='')
    party_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class GuestList(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='guestlist', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, default='')
    party = models.ForeignKey(Party, related_name='guestlist', on_delete=models.CASCADE)
    number_of_guests = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
