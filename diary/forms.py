from django.forms import ModelForm, ValidationError, Textarea
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = Textarea(
            attrs={'rows': 1, 'cols': 25})
        self.fields['description'].widget = Textarea(
            attrs={'rows': 4, 'cols': 35})

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(user=self.user, title=title).exists():
            raise ValidationError(
                "You have already written a post with same title.")
        return title
