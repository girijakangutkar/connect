from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from app.forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from .models import job
from .forms import ApplyForm
from django.contrib import messages
from django.views import View
# Create your views here.


def JobInfo(request):
    job_info = job.objects.all()
    context = {
        'job_info' : job_info
    }
    return render(request, 'app/jobinfo.html', context)


class about(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/about.html')
    
class contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/contact.html')
    
def apply(request):
    if request.method == "POST":
        Apply_form = ApplyForm(request.POST, request.FILES)
        if Apply_form.is_valid():
            Apply_form.save()
            messages.success(request, ('Your Form is submitted'))
        else:
            messages.error(request, 'Error saving form')
        return redirect("JobInfo")
    Apply_form = ApplyForm()
    jobs = job.objects.all()
    return render(request=request, template_name="app/jobform.html", context={'Apply_form':Apply_form, 'jobs':jobs})


@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse_lazy('JobInfo'))

def SignUp(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        

    # This is the render and context dictionary to feed
    return render(request,'app/signup.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse_lazy('JobInfo'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/login.html', {})
