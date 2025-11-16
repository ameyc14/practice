from django import forms
from subjects.models import studentinfo

class StudentForm(forms.ModelForm):
    class Meta:
        model=studentinfo
        fields='__all__'
