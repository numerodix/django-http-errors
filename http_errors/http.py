from django.http import Http404 as http404


class Http302(Exception):
    def __init__(self, url):
        self.url = url

Http404 =  http404
