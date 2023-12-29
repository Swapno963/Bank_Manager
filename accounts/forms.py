from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import ACCOUNT_TYPE, GENDER_TYPE
from django.contrib.auth.models import User
from .models import UserBank, UserAddress



class UserRegistrationForm(UserCreationForm): # user data fillup korbe akta forma but 3 ta model ai fill up hosca
    account_type = forms.CharField(max_length=10,choices=ACCOUNT_TYPE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.CharField(max_length=10, choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=50)

    class Meta:
        model = User 
        fields = ['username','password','password2','first_name','last_name','email','account_type','gender','postal_code','country','birth_date','city','street_address']

    def save(self, commit= True):
        our_user = super().save(commit=False) # datebase a akn false thake save hobe nah
        if commit == True:
            our_user.save() # user model a data save hobe
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')

            UserAddress.objects.create(
                user = our_user,
                street_address = street_address,
                city = city,
                postal_code = postal_code,
                country = country,
            )
            
            UserBank.objects.create(
                user = our_user,
                account_type = account_type,
                gender = gender,
                birth_date = birth_date,
                account_no = 100000 + our_user.id 
            )
