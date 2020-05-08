from django import forms
from Blog.models import Comment,Post

class PostForm(forms.ModelForm):
    class Meta():
        model= Post
        fields=('author','title','text')
class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')
