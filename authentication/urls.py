from unicodedata import name
from django.urls import path
from authentication.views import login_view


urlpatterns = [
    path('login/', login_view.LoginView.as_view(), name='login_view')
]