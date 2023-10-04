from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs = {'rows':5, 'placeholder': 'Write on me!'}
        ),
        max_length = 4000,
        help_text='Max text length should be less than 4000.')

    class Meta:
        model = Topic
        fields = ['subject','message']