from django_filters import rest_framework as filters


class AdStatsFilterSet(filters.FilterSet):
    sdk_version = filters.CharFilter()
    username = filters.CharFilter()
    session_id = filters.CharFilter()
    country_code = filters.CharFilter()
    platform = filters.CharFilter()
