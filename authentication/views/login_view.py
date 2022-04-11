from unicodedata import name
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):

    def post(self,request):
        print(request.POST)
        return JsonResponse({'success':True}, safe=False)