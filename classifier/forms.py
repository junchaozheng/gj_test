from django import forms

from .models import Prediction

class PostForm(forms.ModelForm):

    class Meta:
        model = Prediction
        fields = ('text',)