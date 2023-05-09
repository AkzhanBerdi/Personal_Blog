from django import forms
from website.models import Comment


class GenreForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
        label='Genre name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Input Genre name"
        })
    )
    description = forms.CharField(
        max_length=500,
        min_length=10,
        required=True,
        label='Genre description',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'form-control'
        })
    )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text','author',)