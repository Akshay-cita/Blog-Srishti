from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
 class Post(models.Model):
     author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
     title=models.CharField(max_length=200)
     text=models.TextField()
     create_date=models.DateTimeField(default=timezone.now()) #publish date and time
     published_date=models.DateTimeField(blank=True,null=True)


     def approve_comment(self):
         return self.comments.filter(approved_comment=True)

     def get_absolute_url(self):
         return reverse("post_detail" kwargs={'pk':self.pk})


     def publish(self):
         self.published_date=timezone.now()
         self.save()

     def __str__(self):
         self.title
class Comment(model.Model):
    post=models.ForeignKey('Blog.Post',related_name='comments')
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approved_comment=models.BooleanFeild(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
