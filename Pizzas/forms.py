from django import forms

from .models import *


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        labels = {'text':'Pizza Name'}


#testing comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':'Comment here:'}

        