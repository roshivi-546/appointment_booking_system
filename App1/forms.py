from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import CustomUser
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class RegistrationForm(CustomUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name','email', 'phone', 'profession', 'state_name', 'dist_name', 'image']
        labels = {'name':'Name', 'email':'Email', 'phone':'Phone', 'profession':'Profession', 'state_name':'State', 'dist_name':'District', 'image':'Image', 'password':'Password'}

        widgets = {
                 'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Enter Name Here'}),
                 'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Enter Email Here'}),
                 'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Enter Phone Number Here'}),
                 'profession' : forms.Select(attrs={'class':'form-control'}),
                 'state_name' : forms.Select(attrs={'class':'form-control'}),
                 'dist_name' : forms.Select(attrs={'class':'form-control'}),
                 'image' : forms.FileInput(attrs={'class':'form-control'}),
                 #'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'Password'})
        }

class appointment_booking_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email', 'phone', 'specialist', 'profession', 'state_name', 'dist_name', 'reason']
        labels = {'name':'Name', 'email':'Email', 'specialist':'Specialist Name', 'profession':'Profession', 'state_name':'State', 'dist_name':'District', 'reason':'Reason'}

        widgets = {
                 'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Enter Name Here'}),
                 'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Enter Email Here'}),
                 'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Enter Mobile Number Here'}),
                 'reason' : forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Reason for making an Appointment', 'style': 'height:100px'}),
                 #'remark' : forms.Textarea(attrs={'class':'form-control mt-2', 'placeholder' : 'Enter Your Remark Here'}),
                 'specialist' : forms.Select(attrs={'class':'form-control'}),
                 'profession' : forms.Select(attrs={'class':'form-control'}),
                 'state_name' : forms.Select(attrs={'class':'form-control'}),
                 'dist_name' : forms.Select(attrs={'class':'form-control'}),

                 }


#class loginform(AuthenticationForm):
    #class Meta:
        #model = User
        #fields = ['email', 'password']

        #labels = {'email':'Email', 'password':'Password'}

        #widgets = {
        #     'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Email'}),
        #     'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'Password'})
        #}
