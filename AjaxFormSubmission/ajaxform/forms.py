from django import forms
from ajaxform.models import TinyTest

class TinyFormTest(forms.ModelForm):
    class Meta:
        model = TinyTest
        fields = ('name', 'email', 'created_at')
