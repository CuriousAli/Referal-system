from django.urls import path

from phone.views import *

urlpatterns = [
    path('', enter, name='enter'),
    path('sms/', sms, name='sms'),
    path('profile/', profile, name='profile'),
    path('registration/', Registration.as_view(), name='registration')
]