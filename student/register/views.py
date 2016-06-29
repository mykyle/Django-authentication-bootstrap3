from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import Contact_Form,studentForm
from django.contrib import messages
from .models import student
from django.contrib.auth import authenticate, login

def Index(request):

    return render(request, 'register/index.html')

def Create(request):
    if request.method == 'POST':
        form=Contact_Form(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            secondname=form.cleaned_data['lastname']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=student(firstname=firstname,lastname=secondname,username=username,password=password)
            user.save()
            messages.success(request, 'thanks for registering.')
            return render_to_response('register/signup.html',{'form':form},RequestContext(request))
        else:
            return render(request, 'register/signup.html',{'form':form})
    else:
        form = Contact_Form()
        return render(request, 'register/signup.html',{'form':form})

def login(request):
        if request.method == 'POST':
            form=studentForm(request.POST or None)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, 'details exists.')
                        return HttpResponseRedirect('register/home_page.html')
                    else:
                        messages.error(request, 'your account has been deactivated .')
                        return render_to_response('register/login.html',{'form':form},RequestContext(request))
                else:
                    messages.error(request, 'your details did not match .')
                    return render_to_response('register/login.html',{'form':form},RequestContext(request))
            else:
                messages.error(request, 'your details are invalid .')
                return render_to_response('register/login.html',{'form':form},RequestContext(request))
        else:
            form=studentForm(request.POST or None)
            return render_to_response('register/login.html',{'form':form},RequestContext(request))


def Authorized(request):
    if not request.user.is_authenticated():
        return render(request, 'books/home_page.html')
    else:
        return HttpResponseRedirect("register/login")



def logout_view(request):
    logout(request)
    HttpResponseRedirect('register/create')
