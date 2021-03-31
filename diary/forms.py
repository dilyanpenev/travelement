from django.forms import ModelForm, ValidationError
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(user=self.user, title=title).exists():
            raise ValidationError(
                "You have already written a post with same title.")
        return title
