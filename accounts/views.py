
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method!='POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            
            login(request , new_user)
            messages.success(request, 'Registration successful! You will be redirected shortly.')
            
            # Render the registration page with a flag to trigger SweetAlert
            return render(request, 'registration/register.html', {'form': form, 'registration_success': True})
    
    context={'form': form}
    return render (request , 'registration/register.html' , context)