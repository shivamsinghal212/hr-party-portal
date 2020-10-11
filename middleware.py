import json
from json import JSONDecodeError

from django.http import HttpResponse
from rest_framework import status


class ValidateRequestBody(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method in ["POST", "DELETE"] and request.content_type == 'application/json':
            try:
                body = json.loads(request.body)
            except JSONDecodeError:
                return HttpResponse("Bad request", status=status.HTTP_400_BAD_REQUEST)
            request._body = body
        response = self.get_response(request)
        return response
