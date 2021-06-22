from django import forms
from .models import BoardList

class DateInput(forms.DateInput):
    input_type = 'date'

class BoardForm(forms.ModelForm):
    class Meta:
        model = BoardList
        fields = ('title', 'content', 'end_date')
        widgets = {
            'end_date' : DateInput()
        }
