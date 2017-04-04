from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from guestlist.models import Party, Venue, GuestList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = (
            'url', 'id', 'name', 'street', 'province', 'city', 'postal_code', 'apartment', 'country', 'created')
        read_only_fields = ('created',)


class PartySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Party
        fields = ('url', 'id', 'owner', 'name', 'venue', 'description', 'party_date', 'created')
        read_only_fields = ('created',)

    def validate(self, data):
        party_date = data['party_date']
        if party_date < timezone.now():
            raise serializers.ValidationError("Party cannot be created for past")
        return data


class GuestListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GuestList
        fields = ('url', 'owner', 'name', 'party', 'number_of_guests', 'created')
        read_only_fields = ('created',)
