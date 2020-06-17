from django import forms
from .models import News
class newsFormAdd(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

