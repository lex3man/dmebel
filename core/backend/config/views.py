from django.http import JsonResponse, HttpResponse
from django.views import View
import json


class VKrequest(View):
    def post(self, req):
        request = json.loads(req.body)
        if request['type'] == 'confirmation':
            return HttpResponse('a817ff9d')
