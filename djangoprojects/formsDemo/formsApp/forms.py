from django import forms
from django.core import validators
class UserRegistrationForm(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstname=forms.CharField(required=False,validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    lastname=forms.CharField()
    email=forms.CharField()
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password=forms.CharField(widget=forms.PasswordInput)
    ssn=forms.IntegerField()

#
def clean_firstName(self):
    inputFirstName=self.cleaned_data['firstname']
    if len(inputFirstName)>20:
        raise forms.ValidationError('the max length of firstname is 20 characters')
    return inputFirstName

# def clean(self):
#     user_cleaned_data=super().clean()
#     inputFirstName=user_cleaned_data['firstname']
#     if len(inputFirstName)>20:
#             raise forms.ValidationError('the max length of firstname is 20 characters')
