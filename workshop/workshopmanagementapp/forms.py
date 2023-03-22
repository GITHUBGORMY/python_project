from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from workshopmanagementapp.models import Login,  manager, worker
from django import forms

class workerForm(forms.ModelForm):
    class Meta:
        model= worker
        fields = "__all__"
        exclude = ("customer",)
class managerForm(forms.ModelForm):
    class Meta:
        model = manager
        fields = "__all__"
        exclude = ("customer",)
class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')