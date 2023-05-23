from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User 
# from tinymce.models import HTMLField
# Create your models here.
from django.utils.timezone import now
# Category model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image= models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
     return f"{self.title}"
    def image_tag(self):
       return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.image))
       


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='post/')

    





    def __str__(self):
     return f"{self.title}"
    def image_tag1(self):
      return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.image))
    

# class Comment(models.Model):
   
#    comments=models.TextField(max_length=250,primary_key=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    date = models.DateField(auto_now_add=True)
#    post = models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE, default="",null=True)

#    def __str__(self):
#      return f"{self.comments}"
   




class Comment(models.Model):
   name=models.CharField(max_length=200,default="")
   comment=models.TextField(max_length=200,default="")
   email=models.EmailField()
   date=models.DateTimeField(auto_now_add=True,null=True)   
   post = models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE, default="",null=True)
   def __str__(self):
     return f"{self.name}"

