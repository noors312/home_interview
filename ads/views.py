# Create your views here.
from pyexpat import ExpatError

import requests
import xmltodict
from django.conf import settings
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from ads.filters import AdStatsFilterSet
from ads.models import AdRequest, Impression
from ads.serializers import (
    GetAdRequestSerializer,
    AdStatsSerializer,
    AdDataSerializer,
    ImpressionSerializer,
)


class GetAdAPIView(APIView):
    request_serializer = GetAdRequestSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.request_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        ad_response = requests.get(
            settings.VAST_API_URL
        )  # decode to get string instead of bytes
        try:
            ad_data = self.parse_xml(ad_response.content.decode())
        except (ExpatError, ValidationError) as e:
            ad_data = {"duration": 0, "media_files": None, "error": "XML is invalid"}
        AdRequest(**ad_data, **serializer.validated_data).save()
        return HttpResponse(ad_response)

    def parse_xml(self, xml_data: str) -> dict:
        """
        Here I use xmltodict package to parse XML data to dict cause it's easier work with dict
        :param xml_data: XML data as string got from VAST API
        :return: dict {'duration': int, 'media_files': url}
        """
        data = xmltodict.parse(xml_data)
        ad_data = data.get("VAST").get("Ad").get("InLine")
        serializer = AdDataSerializer(data=ad_data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data


class ImpressionCreateAPIView(CreateAPIView):
    model = Impression
    serializer_class = ImpressionSerializer


class GetStatsAPIView(ListAPIView):
    serializer_class = AdStatsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdStatsFilterSet

    def list(self, request, *args, **kwargs):
        """
        Here I use ListAPIView instead of RetrieveAPIView to get self.filter_queryset() method.
        It helps to easily filter queryset by query_params
        """

        ad_requests = self.filter_queryset(AdRequest.objects.all())
        impressions = self.filter_queryset(Impression.objects.all())
        impressions_count = impressions.count()
        ad_requests_count = ad_requests.count()
        try:
            fill_rate = impressions_count / ad_requests_count
        except ZeroDivisionError:
            fill_rate = impressions_count

        response = {
            "impression_per_client": impressions_count,
            "ad_per_client": ad_requests_count,
            "fill_rate": round(fill_rate, 2),
        }
        serializer = self.serializer_class(data=response)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=200)
