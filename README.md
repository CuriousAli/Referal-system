This little project is part of test task, but i wanted to make complete referal system.

Installation:
pip install -r requirements.txt (Load modules from requirements.txt)

Launch project:
python manage.py runserver

Main logic:

Creation if referal code for new user 
location: phone/views.py

@login_required
def profile(request):
    form = ReferalForm()
    pk = request.session.get('pk')
    user = User.objects.get(pk=pk)
    if user.my_ref == (0 or "0"):
        user.my_ref = generate_code(6)
        user.save()

Applying referal code of other user(allowed only one time)
location: phone/views.py def profile

if request.method == 'POST':
    referal = request.POST.get('inv_ref')
    if referal != user.my_ref:
        if User.objects.get(my_ref=referal):
            user.inv_ref = referal
            user.save()
            redirect('profile')

Shows users which applied the user's referal code
location: phone/views.py def profile

ref_list = User.objects.filter(inv_ref=own_ref)

Login and registration method realised by build-ins django functions

Autintication through sms number verification thanks a lot to Pyplane's YT tutorrial
https://www.youtube.com/watch?v=YA4ZPKTPicw

