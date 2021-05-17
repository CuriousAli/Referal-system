from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from phone.forms import ReferalForm
from phone.models import User
from phone.utils import delay_func
from sms.forms import SmsForm


def enter(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        number = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, number=number, password=password)
        if User.objects.filter(number=number) == []:
            new_user = User(number=number, password=password)
            new_user.save()

        user = authenticate(request, number=number, password=password)

        if user is not None:
            request.session['pk'] = user.pk
            return redirect('sms')

    return render(request, 'phone/enter.html', {'form': form})


def sms(request):
    form = SmsForm(request.POST or None)
    delay_func(2)
    redirect('profile')

    return render(request, 'sms/sms.html', {'form': form})


@login_required
def profile(request):
    form = ReferalForm()
    pk = request.session.get('pk')
    user = User.objects.get(pk=pk)
    own_ref = user.my_ref
    if request.method == 'POST':
        referal = request.POST.get('inv_ref')
        if referal != user.my_ref and User.objects.filter(my_ref=referal) != []:
            user.inv_ref = referal
            user.save()
            redirect('profile')

    ref_list = User.objects.filter(inv_ref=own_ref)

    return render(request, 'phone/profile.html', {'form': form, 'own_ref': own_ref, 'ref_list': ref_list, 'user': user})


