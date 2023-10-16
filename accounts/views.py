from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import forms, authenticate, login

def profile(request):
    return HttpResponseRedirect('/accounts/profile')

def signup(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            new_account = form.save()
            new_account = authenticate(username = form.cleaned_data['username'],
                                        password = form.cleaned_data['password1'],
                                        )
            login(request, new_account)
            return HttpResponseRedirect('/')
    else:
        form = forms.UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})