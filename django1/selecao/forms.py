from django import forms
from . import models


class CalcForm(forms.Form):
   pass



class MessageForm(forms.ModelForm):


    class Meta:
        model = models.Message
        fields = [
            'email',
            'title',
            'content',
            'creator',
        ]
