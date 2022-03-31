# Interview project

## How to start application

```shell
git clone https://github.com/noors312/home_interview.git

cd home_interview

docker-compose up -d
```

### URLS

[GetAd](http://localhost:8000/api/v1/get_ad) - to create AdRequest and get VAST API response

[GetStats](http://localhost:8000/api/v1/get_stats) - get stats about Impressions and AdRequest

[GetStats](http://localhost:8000/api/v1/impression) - to create Impression

### SOME DESCRIPTION ABOUT PROJECT DESIGN AND CODE

Here is default Django application with default project design. I choose Django because it's easy to set up new project
and make CRUD application which it is. Here I use default `APIView, CreateAPIView, ListAPIVIew` classes provided
by `Django REST Framework`. Also, I added `xmltodict` package to parse XML from VAST API into dict, and work on it
easier, and `django-filter` to filter data for views. `FactoryBoy` and `Faker` by default for testcases.
In `home_interview/ads/serializers.py` I described `GetAdRequestSerializer` to validate query params provided to
endpoint, and make sure that `username` or `sdk_version` were provided. `AdDataSerializer` to validate XML data from
VAST API, because I don't know the business logic if data format is changed, so I need to validate only one case.
Also `AdDataSerializer` returns prepared data to create `AdRequest` instance and store it in DB. I wrote some docstring
in views, so I hope it will be easy to read and understand.

### NOTE

* Please do not be confused by envs/*.env files, it's just for test and run application via docker, in production it
  will be changed of course