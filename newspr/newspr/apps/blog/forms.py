from django import forms
from blog.models import *

class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control','placeholder':'Текст комментария'})
        }