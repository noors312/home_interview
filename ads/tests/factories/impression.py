import random

import factory

from ads.models import Impression


class ImpressionFactory(factory.DjangoModelFactory):
    username = factory.Faker("name")
    sdk_version = factory.Faker("pyint")
    country_code = factory.Faker("country_code")
    session_id = factory.Faker("pyint")
    platform = factory.Sequence(
        lambda x: random.choice(["MacOS", "IOS", "Android", "Windows", "Linux"])
    )

    class Meta:
        model = Impression
