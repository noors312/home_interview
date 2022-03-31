from rest_framework import serializers

from ads.models import Impression


# noinspection PyAbstractClass
class GetAdRequestSerializer(serializers.Serializer):
    SDK_version = serializers.CharField(
        allow_blank=True, allow_null=True, required=False, source="sdk_version"
    )
    session_id = serializers.CharField(
        allow_blank=True, allow_null=True, required=False
    )
    username = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    platform = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    country_code = serializers.CharField(
        allow_blank=True, allow_null=True, required=False
    )

    def validate(self, attrs):
        super(GetAdRequestSerializer, self).validate(attrs)
        if not any([attrs.get("sdk_version"), attrs.get("username")]):
            raise serializers.ValidationError(
                "You should provide either SDKVersion or username"
            )
        return attrs


# noinspection PyAbstractClass
class ImpressionSerializer(serializers.ModelSerializer):
    SDK_version = serializers.CharField(
        allow_blank=True, allow_null=True, required=False, source="sdk_version"
    )
    session_id = serializers.CharField(
        allow_blank=True, allow_null=True, required=False
    )
    username = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    platform = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    country_code = serializers.CharField(
        allow_blank=True, allow_null=True, required=False
    )

    class Meta:
        model = Impression
        fields = (
            "SDK_version",
            "session_id",
            "username",
            "platform",
            "country_code",
        )


# noinspection PyAbstractClass
class VASTAdInfoSerializer(serializers.Serializer):
    Duration = serializers.TimeField(format="%H:%M:%S", source="duration")
    MediaFiles = serializers.DictField(source="media_files")

    def validate_Duration(self, value):
        seconds = value.hour * 3600 + value.minute * 60 + value.second
        return seconds

    def validate_MediaFiles(self, value):
        return value.get("MediaFile")


# noinspection PyAbstractClass
class VASTLinearTagSerializer(serializers.Serializer):
    Linear = VASTAdInfoSerializer(source="linear")


# noinspection PyAbstractClass
class VASTCreativeSerializer(serializers.Serializer):
    Creative = VASTLinearTagSerializer(source="creative")


# noinspection PyAbstractClass
class AdDataSerializer(serializers.Serializer):
    Creatives = VASTCreativeSerializer(source="creatives")
    Error = serializers.CharField(source="error", allow_null=True, allow_blank=True)

    def validate(self, attrs):
        super(AdDataSerializer, self).validate(attrs)
        response = {
            "duration": attrs.get("creatives").get("creative").get("linear").get("duration"),
            "media_files": attrs.get("creatives").get("creative").get("linear").get("media_files"),
            "error": attrs.get("error"),
        }
        return response


# noinspection PyAbstractClass
class AdStatsSerializer(serializers.Serializer):
    impression_per_client = serializers.DecimalField(
        decimal_places=2, max_digits=15, required=False
    )
    ad_per_client = serializers.DecimalField(
        decimal_places=2, max_digits=15, required=False
    )
    fill_rate = serializers.DecimalField(decimal_places=2, required=False, max_digits=2)
