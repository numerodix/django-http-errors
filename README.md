django-http-errors
=============

Custom http error classes for Django

Install
-------

    $ pip install -e git://github.com/numerodix/django-http-errors.git#egg=django-http-errors

Then add:

```python
INSTALLED_APPS = (
    ..
    'http_errors',
    ..
)
```

```python
MIDDLEWARE_CLASSES = (
    ..
    'http_errors.middleware.HandleHttpErrorsMiddleware',
    ..
)
```

How to use
----------

```python
from http_errors.http import Http302

def some_view(request):
    raise Http302('http://some/url')
```
