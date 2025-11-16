from django.shortcuts import render
from .import forms
# Create your views here.
def userRegistrationView(request):
    form=forms.UserRegistrationForm()
    if request.method=='POST':
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            print("Firstname:",form.cleaned_data['firstname'])
            print("lastname:",form.cleaned_data['lastname'])
            print("email:",form.cleaned_data['email'])


    return render(request,'formsDemo/userRegistration.html',{'form':form})
