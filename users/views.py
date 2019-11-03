from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    #check for Post request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congatulations, {username}!')
            return redirect('blog-home')

    else:
        form = UserRegisterForm() #create an insance of UserCreationForm

    return render(request, 'users/register.html', {'form':form})

#messages.debug
#messages.info
#messages.success
