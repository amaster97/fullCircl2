from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from .models import EDUCATION_LEVELS, INDUSTRIES, REGIONS



class SeekerSignUpForm(UserCreationForm):
	First_Name = forms.CharField(max_length=30)
	Last_Name = forms.CharField(max_length=30)
	Email = forms.EmailField(max_length=254)
	Birth_Date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

	Bio = forms.CharField(max_length=500)
	Profile_Picture = forms.ImageField(required=False)

	Education_Level = forms.CharField(max_length=15, widget=forms.Select(choices=EDUCATION_LEVELS))
	Education_Level_Priority = forms.IntegerField()
	Institution = forms.CharField(max_length=60)
	
	Sponsorship = forms.BooleanField(required=False)
	Sponsorship_Priority = forms.IntegerField()
	
	Skills = forms.CharField()
	Skills_Priority = forms.IntegerField()

	Industry = forms.CharField(max_length=20, widget=forms.Select(choices= INDUSTRIES))
	Industry_Priority = forms.IntegerField()

	Location = forms.CharField(max_length=20, widget=forms.Select(choices= REGIONS))
	Location_Priority = forms.IntegerField()

	isSeeker = True;

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'First_Name', 'Last_Name', 'Email', 'Birth_Date', 'Bio', 'Profile_Picture', 'Education_Level', 'Education_Level_Priority', 'Institution', 'Sponsorship', 'Sponsorship_Priority', 'Skills', 'Skills_Priority', 'Industry', 'Industry_Priority', 'Location', 'Location_Priority')

class RecruiterSignUpForm(UserCreationForm):
	First_Name = forms.CharField(max_length=30)
	Last_Name = forms.CharField(max_length=30)
	Email = forms.EmailField(max_length=254)
	Birth_Date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

	Bio = forms.CharField(max_length=500)
	Profile_Picture = forms.ImageField(required=False)

	Education_Level = forms.CharField(max_length=15, widget=forms.Select(choices=EDUCATION_LEVELS))
	Education_Level_Priority = forms.IntegerField()
	Institution = forms.CharField(max_length=60)
	
	Sponsorship = forms.BooleanField(required=False)
	Sponsorship_Priority = forms.IntegerField()
	
	Skills = forms.CharField()
	Skills_Priority = forms.IntegerField()

	Industry = forms.CharField(max_length=20, widget=forms.Select(choices= INDUSTRIES))
	Industry_Priority = forms.IntegerField()

	Location = forms.CharField(max_length=20, widget=forms.Select(choices= REGIONS))
	Location_Priority = forms.IntegerField()

	isSeeker = False;

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'First_Name', 'Last_Name', 'Email', 'Birth_Date', 'Bio', 'Profile_Picture', 'Education_Level', 'Education_Level_Priority', 'Institution', 'Sponsorship', 'Sponsorship_Priority', 'Skills', 'Skills_Priority', 'Industry', 'Industry_Priority', 'Location', 'Location_Priority')


