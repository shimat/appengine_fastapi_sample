# appengine_fastapi_sample
AppEngine(Standard Environment) + Python3.8 + FastAPI

```sh
$ pip install fastapi uvicorn[standard] gunicorn
$ pip freeze > requirements.txt
$ gcloud app deploy app.yaml --project *** --promote
```

## Prerequisites
- Ubuntu 20.04/18.04
  - `uvloop` does not seem to support Windows

## References
### FastAPI + AppEngine
- https://medium.com/analytics-vidhya/deploying-fastapi-application-in-google-app-engine-in-standard-environment-dc061d3277a
- https://github.com/encode/uvicorn/blob/master/CHANGELOG.md#0120---2020-09-28

### IAP
- https://cloud.google.com/iap/docs/authentication-howto#iap_make_request-python
- https://medium.com/google-cloud-jp/gae-2nd-gen-%E3%81%A7%E3%81%AE%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E9%96%93%E8%AA%8D%E8%A8%BC-1ed1d8b1abce
- https://qiita.com/mag-chang/items/82d0aefbd988e4d749f2
