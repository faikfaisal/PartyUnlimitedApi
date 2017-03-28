from django.contrib.auth.models import User
from rest_framework import serializers

from guestlist.models import Party, Venue, GuestList


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = (
            'url', 'id', 'name', 'street', 'province', 'city', 'postal_code', 'apartment', 'country', 'created')


class PartySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Party
        fields = ('url', 'id', 'owner', 'name', 'venue', 'description', 'party_date', 'created')


class GuestListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GuestList
        fields = ('url', 'owner', 'name', 'party', 'number_of_guests')
