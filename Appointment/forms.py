from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField







class Registration(forms.ModelForm):
    class  Meta:
        model = Accounts
        fields = ('email','password','is_patient')


class add_patient(forms.ModelForm):
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control col-md-6'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control col-md-6'}))

    class Meta:
        model = Patient
        
        fields = '__all__'
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Patient
        fields = '__all__'
    def clean_password(self):
        return self.initial["password"]


class Updatehos(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = "__all__"


class Updatedoc(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"