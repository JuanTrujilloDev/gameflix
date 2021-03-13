from django import forms
from .models import Comment
class NewComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
          'content': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }