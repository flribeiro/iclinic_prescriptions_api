<p align="center">
  <img src="medic.jpg" width="220" alt="iClinic Challenge" />
</p>

# BackEnd Challenge - iClinic

API developed as challenge for a backend job position at iClinic.

## Choices

- Python
- Django with Django REST Framework
- Docker
- PostgreSQL
- Redis

## Environment variables needed to execute the application

```
SECRET_KEY=******
DJANGO_SETTINGS_MODULE=iclinic.settings
APP_PORT=8000
DB_NAME=postgres
DB_USER=postgres
DB_PASSWD=******
DB_HOST=db
DB_PORT=5432
REDIS_LOCATION=redis://redis_dev:6379/1
PHYSICIANS_API_URL=https://5f71da6964a3720016e60ff8.mockapi.io/v1
PHYSICIANS_API_PATH=/physicians/{id}
PHYSICIANS_API_TOKEN=******
PHYSICIANS_API_TIMEOUT=4
PHYSICIANS_API_RETRY=2
PHYSICIANS_API_CACHE_TTL_HOURS=48
CLINICS_API_URL=https://5f71da6964a3720016e60ff8.mockapi.io/v1
CLINICS_API_PATH=/clinics/{id}
CLINICS_API_TOKEN=******
CLINICS_API_TIMEOUT=5
CLINICS_API_RETRY=3
CLINICS_API_CACHE_TTL_HOURS=72
PATIENTS_API_URL=https://5f71da6964a3720016e60ff8.mockapi.io/v1
PATIENTS_API_PATH=/patients/{id}
PATIENTS_API_TOKEN=******
PATIENTS_API_TIMEOUT=3
PATIENTS_API_RETRY=2
PATIENTS_API_CACHE_TTL_HOURS=12
METRICS_API_URL=https://5f71da6964a3720016e60ff8.mockapi.io/v1
METRICS_API_PATH=/metrics
METRICS_API_TOKEN=******
METRICS_API_TIMEOUT=6
METRICS_API_RETRY=5
```

## Setup / running the app
### Clone project:
```bash
$ git clone https://github.com/flribeiro/iclinic_prescriptions_api
```

### Pre-requisites:
* To have the `.env` file (sent by e-mail) present at the project's root directory;
* To have `docker` and `docker-compose` installed.

### Being at the project's root folder:
```bash
$ make build
```


## API Documentation

The endpoint to post prescriptions will be available at
```text
http://localhost:8000/prescriptions/
```

## Test
```bash
# unit tests
$ make test
```

After run the tests, coverage report will be available at `htmlcov/index.html` (open in browser).


## cURLs for calling API
### POST /prescriptions/:
```text
curl --location --request POST 'http://localhost:8000/prescriptions/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "clinic": {
    "id": 1
  },
  "physician": {
    "id": 1
  },
  "patient": {
    "id": 1
  },
  "text": "Medication"
}'
```
Output body sample:
```
{
  "data": {
    "id": 1,
    "clinic": {
      "id": 1
    },
    "physician": {
      "id": 1
    },
    "patient": {
      "id": 1
    },
    "text": "Dipirona 1x ao dia"
  }
}
```


---

## _"Thanks for the opportunity."_ ~ [Fabrício L. Ribeiro](http://t.me/flribeiro)
