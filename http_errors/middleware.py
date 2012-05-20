from django.http import HttpResponseRedirect

from http import Http302


class HandleHttpErrorsMiddleware(object):
    def process_exception(self, request, exception):
        if isinstance(exception, Http302):
            return HttpResponseRedirect(exception.url)
