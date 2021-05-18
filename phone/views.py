from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from phone.forms import *
from phone.models import User
from phone.utils import delay_func, generate_code
from sms.forms import SmsForm


class Registration(CreateView):
    form_class = CustomRegForm
    template_name = 'phone/registration.html'
    success_url = reverse_lazy('enter')


def enter(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        number = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, number=number, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('sms')

    return render(request, 'phone/enter.html', {'form': form})


def sms(request):
    form = SmsForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = User.objects.get(pk=pk)
        code = user.sms_code
        code_user = f"{user.number}: {user.sms_code}"
        if not request.POST:
            delay_func(2)
            redirect('profile')
            print(code_user)
        if form.is_valid():
            num = form.cleaned_data.get('auto_code')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('profile')
            else:
                return redirect('enter')

    return render(request, 'sms/sms.html', {'form': form, 'code': code})


@login_required
def profile(request):
    form = ReferalForm()
    pk = request.session.get('pk')
    user = User.objects.get(pk=pk)
    if user.my_ref == (0 or "0"):
        user.my_ref = generate_code(6)
        user.save()
    own_ref = user.my_ref
    if request.method == 'POST':
        referal = request.POST.get('inv_ref')
        if referal != user.my_ref:
            if User.objects.get(my_ref=referal):
                user.inv_ref = referal
                user.save()
                redirect('profile')

    ref_list = User.objects.filter(inv_ref=own_ref)

    return render(request, 'phone/profile.html', {'form': form, 'own_ref': own_ref, 'ref_list': ref_list, 'user': user})



