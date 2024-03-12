import datetime
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class BookingForm(forms.Form):
        name = forms.ModelChoiceField(queryset = CommunityCenter.objects.all())
        date = forms.DateField(widget=forms.SelectDateWidget)

class BookingGroundForm(forms.Form):
        name = forms.ModelChoiceField(queryset = PlayGround.objects.all())
        date = forms.DateField(widget=forms.SelectDateWidget)

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

class Meta:
	model = User
	fields = ( "first_name", "last_name", "email", "username")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user