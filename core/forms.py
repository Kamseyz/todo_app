from django import forms
from .models  import TODO


class TODOFORM(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ('title', 'content')