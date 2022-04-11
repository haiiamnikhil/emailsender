from django.http import JsonResponse
from emaildispatcher.models import *
from django.forms.models import model_to_dict


def retrieve_email(request):
    if request.method == 'GET':
        saved_emails = Emails.objects.values('emails')
        print(saved_emails['emails'])
        return JsonResponse({'emails':saved_emails['emails']})