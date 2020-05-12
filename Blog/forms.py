from django.contrib.auth.models import User
from django import forms
from Blog.models import Comment,Post,UserProfileInfo

class PostForm(forms.ModelForm):
    class Meta():
        model= Post
        fields=('author','title','text')
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model= User
        fields=('username','email','password')
class UserProfileInfoform(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
