from django.urls import path
from emaildispatcher.views.email_view import *
from emaildispatcher.views.ajax import email_retriever_ajax

urlpatterns  = [
    path('', Send.as_view(), name='send_email'),
    path('get-emails/', email_retriever_ajax.retrieve_email, name="retrieve_emails")
]