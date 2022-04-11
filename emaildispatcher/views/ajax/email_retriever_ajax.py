from django.http import JsonResponse
from emaildispatcher.models import *
from django.forms.models import model_to_dict


def retrieve_email(request):
    if request.method == 'GET':
        saved_emails = Emails.objects.all().order_by('-pk').first()
        print(saved_emails)
        return JsonResponse(list(saved_emails.values('emails')), safe=False)