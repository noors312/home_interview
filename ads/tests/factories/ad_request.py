import random
import string

import factory

from ads.models import AdRequest


class AdRequestFactory(factory.DjangoModelFactory):
    username = factory.Faker('name')
    sdk_version = factory.Faker('pyint')
    country_code = factory.Faker('country_code')
    session_id = factory.Faker('pyint')
    platform = factory.Sequence(lambda x: random.choice(['MacOS', 'IOS', 'Android', 'Windows', 'Linux']))
    error = factory.Sequence(lambda x: ''.join(random.choices(string.ascii_letters, k=20)))
    duration = factory.Sequence(lambda x: random.choice(range(1, 100)))
    media_files = factory.Faker('image_url')

    class Meta:
        model = AdRequest
