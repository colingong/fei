from django import forms
from django.shortcuts import render, HttpResponse

class CreateAccount(forms.Form):
    user_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    password = forms.PasswordInput()
    phone = forms.CharField()
    pay_password = forms.PasswordInput()

def create_user(request):
    if request.method == 'GET':
        form = CreateAccount()
        return render(request, 'account/create_user.html', {'form': form})
    elif request.method == 'POST':
        for k, v in request.POST.items():
            print(f'{k} --- {v}')
        return HttpResponse('you POST')
    else:
        return HttpResponse('should be GET or POST')