import django_filters

from guestlist.models import Party


class PartyFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_expr="contains")

    class Meta:
        model = Party
        fields = ['name', 'is_active']
