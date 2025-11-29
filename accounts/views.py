from django.shortcuts import render, redirect
from django.contrib.auth import login , logout , authenticate # django inbuilt operation that return true or false
from django.contrib.auth.decorators import login_required# returns true or false -> gives permission to usage of view actions based off user login activities 
# decorator is when function return another function
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.urls import reverse_lazy
from . forms import UserRegistrationForm,UserLoginForm,UserProfileForm

# Create your views here.
def register_view(request):
    #validate if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('media_assets:dashboard')

    if request.method == 'POST': # user wants to register
        form = UserRegistrationForm(request.POST)
        #if user has filled all required inputs
        if form.is_valid():
            user = form.save()  ## submit our user to db
            login(request,user)  ## calls the login action
            messages.success(request,f'Welcome {user.username}! Your account has been successfully created!')
            return redirect('media_assets:dashboard')
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form = UserRegistrationForm() #dafault http method here is GET
    return render(request, 'accounts/register.html',{'form' : form})

def login_view(request):
    #validate if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('media_assets:dashboard')

    if request.method == 'POST': # user wants to register
        # AuthenticationForm (and subclasses) expect the request as the first arg
        form = UserLoginForm(request, data=request.POST)
        #if user has filled all required inputs
        if form.is_valid():
            # pick up entries for the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #django method to authenthicate and login the user
            user = authenticate(request=request, username=username, password=password) # queries db looking for the user with mentioned credentials
            # if user not found in db
            if user is not None:
                login(request,user)
                messages.success(request, f'Welcome back {username}')
                return redirect('media_assets:dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            # Show actual form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
       
    else: 
        form = UserLoginForm(request) #dafault http method here is GET
    return render(request, 'accounts/login.html',{'form' : form})

## logout -> check if our user is logged in - @login_required
# if user is in then allow this action to run for the user
@login_required
def logout_view(request):
    # use django inbuilt call
    logout(request)
    messages.info(request,f"You have logged out!!")
    return redirect ('accounts:login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES, instance=request.user)
        messages.success(request,f"Profile saved successfully")
        return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'accounts/profile.html',{'form': form})

class CustomPasswordResetView(PasswordResetView):
    # interface change
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset-done') # this will launch the done view

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    # interface change
    template_name= 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete') # this will launch when password is updated

