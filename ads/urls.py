from django.urls import path

from ads.views import GetAdAPIView, GetStatsAPIView, ImpressionCreateAPIView

urlpatterns = [
    path("get_ad", GetAdAPIView.as_view(), name="get_ad"),
    path("get_stats", GetStatsAPIView.as_view(), name="get_stats"),
    path("impression", ImpressionCreateAPIView.as_view(), name="get_ad"),
]
