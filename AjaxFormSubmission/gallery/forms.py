from django import forms
from gallery.models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'comment', 'created_at')
