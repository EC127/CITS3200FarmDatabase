from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import AccessRequestForm
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from accounts.models import User
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = AccessRequestForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('first_name') + " " + form.cleaned_data.get('last_name')
            role = form.cleaned_data.get('role')
            # login(request, user)
            send_mail(
                '[Ridgefield Database] New access request from: {}'.format(email),
                'REQUEST DETAILS\n\nName:\n\t{}\n\nEmail:\n\t{}\n\nRole:\n\t{}'.format(name, email, role),

                #put the emails you wish to use below
                'randomuser@gmail.com',     # Sender email, should be the same as the one in settings.py
                ['randomuser@student.uwa.edu.au'],       # Receiving email for the notifications
                
                fail_silently=False,
            )
            return redirect('submitted')
    else:
        form = AccessRequestForm()
    return render(request, 'registration/register.html', {'form': form})


def submitted(request):
    return render(request, 'registration/request_sent.html')


@staff_member_required
def audit_list(request):
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append(user.to_dict())
    return render(request, 'registration/audit_account.html', {'users': users})


@staff_member_required
def audit_activate(request, pk):
    user = User.objects.get(id=int(pk))
    user.is_active = 1
    user.save()
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append(user.to_dict())
    return render(request, 'registration/audit_account.html', {'users': users})


@staff_member_required
def audit_freeze(request, pk):
    user = User.objects.get(id=int(pk))
    user.is_active = 0
    user.save()
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append(user.to_dict())
    return render(request, 'registration/audit_account.html', {'users': users})

@staff_member_required
def confirm_deletion(request, pk):
    user = User.objects.get(id=pk)
    context =  {'user': user}
    return render(request, "registration/confirm_deletion.html", context)

@staff_member_required
def delete_account(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('audit_list')

