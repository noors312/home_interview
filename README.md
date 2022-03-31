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

### NOTE

* Please do not be confused by envs/*.env files, it's just for test and run application via docker, in production it
  will be changed of course