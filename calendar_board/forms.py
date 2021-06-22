from django import forms
from .models import BoardList

class BoardForm(forms.ModelForm):
    class Meta:
        model = BoardList
        fields = ('title', 'content', 'end_date')
