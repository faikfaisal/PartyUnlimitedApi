from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.filters import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from guestlist.filters import PartyFilter
from guestlist.models import Party, Venue, GuestList
from guestlist.permissions import IsStaff, IsStaffOrReadOnly
from guestlist.serializer import PartySerializer, UserSerializer, VenueSerializer, GuestListSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'parties': reverse('party-list', request=request, format=format),
        'venues': reverse('venue-list', request=request, format=format),
        'guestlist': reverse('guestlist-list', request=request, format=format),
    })


@api_view(['POST'])
def register_user(request):
    serializer_context = {
        'request': request,
    }
    serialized = UserSerializer(data=request.data, context=serializer_context)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.data['username'],
            serialized.data['email'],
            serialized.data['password']
        )
        return Response(serialized.data, status=HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsStaff,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsStaff,)


class GuestListList(generics.ListCreateAPIView):
    queryset = GuestList.objects.all()
    serializer_class = GuestListSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GuestListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GuestList.objects.all()
    serializer_class = GuestListSerializer
    permission_classes = (IsAuthenticated,)


class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = (IsStaff,)


class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = (IsStaff,)


class PartyList(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PartyFilter
    permission_classes = (IsStaffOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PartyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = (IsStaffOrReadOnly,)
