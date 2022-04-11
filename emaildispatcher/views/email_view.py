from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from emaildispatcher.models import *


@method_decorator(csrf_exempt, name="dispatch")
class Send(View):
    template_name = 'sendemail/sendemail.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.is_ajax():
            try:
                params = request.POST
                email_list = params.getlist('emails[]')
                data = {'emails':email_list}
                Emails.objects.create(**data)
                return JsonResponse({'success':True})
            except Exception as e:
                print(e)