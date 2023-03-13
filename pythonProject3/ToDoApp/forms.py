from django import forms

from ToDoApp.models import Todo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("__all__")

