from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import profession, state, dist, CustomUser, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime
from django.template import Context
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .forms import appointment_booking_form
from django.contrib.auth import authenticate,logout as auth_logout, login as auth_login
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from email.message import EmailMessage
from django.conf import settings
from django.views.generic import ListView


# Create your views here.
def index(request):
    if request.method == 'POST':
        fm = appointment_booking_form(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('index')
    else:
        fm = appointment_booking_form()
        print(request.session.get('appointment'))
        print(request.session.get('Date_1'))
        print(request.session.get('email'))
        
    return render(request, 'app1/index.html', {'form':fm})
    messages.SUCCESS(request, "Thanks for makimg an appointment with us. We will email you ASAP")

@login_required
def Appointment_List(request):
    user = User.objects.all().order_by('accepted')
    paginator = Paginator(user, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method=="POST":
        date_1 = request.POST.get('Date')

        appointment_id = request.POST.get('appointment-id')
        appointment = User.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = date_1
        appointment.save()
        request.session['appointment']=appointment_id
        request.session['Date_1']=date_1
        print(request.session.get('appointment'))
        print(request.session.get('Date_1'))
        print(request.session.get('email'))

        #data = {
        #    "name":User.name,
        #    "date":date_1,
        #    "specialist":CustomUser.name,
        #    "reason":User.reason
        #}

        #message = get_template('app1/email.html').render(data)
        #email=EmailMessage(
        #        "About Your Appointment." ,
        #         message,
        #         settings.EMAIL_HOST_USER,
        #         [appointment.email]
        #)
        #email.content_subtype="html"
        #email.send()

    return render(request, 'app1/Appointment_List.html', {'page_obj':page_obj})


#class Appointment_List(ListView):
    #template_name = "app1/appointment_list.html"
    #model = User
    #context_object_name = "appointments"
    #login_required = True
    #ordering = ['accepted#']
    #paginate_by = 3


    #def post(self, request):
        #date = request.POST.get("date")
        #appointment_id = request.POST.get("appointment-id")
        #appointment = User.objects.get(id=appointment_id)
        #appointment.accepted = True
        #appointment.accepted_date = date
        #appointment.save()

        #data = {
            #"name":User.name,
            #"date":date,
            #"specialist":CustomUser.name,
            #"reason":User.reason
        #}

        #message = get_template('app1/email.html').render(data)
        #email=EmailMessage(
            #"About your appointment",
            #message,
            #settings.EMAIL_HOST_USER,
            #[User.email],
        #)
        #email.content_subtype = "html"
        #email.send()
        #return HttpResponseRedirect(request.path)




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'app1/sign_up.html', {'form' : form})

def login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request = request, data = request.POST)
        if fm.is_valid():
            uemail = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(email = uemail, password = upass)
            if user is not None:
                auth_login(request, user)
                request.session['email'] = user.email
                messages.success(request, "Logged in Successfully!..")
                return HttpResponseRedirect("list")
    else:
        fm = AuthenticationForm()
    return render(request, 'app1/login.html', {'form':fm})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("login")

def Profile(request):
    data = CustomUser.objec
    return render(request, 'app1/profile.html')


def Contact(request):
    #user = User.objects.all()
    return render(request, 'app1/contact_us.html')

def Services(request):
    #user = User.objects.all()
    return render(request, 'app1/services.html')

def Home(request):
    return render(request, "app1/home.html")
