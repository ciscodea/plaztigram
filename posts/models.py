from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


""" Post models. """
class Post(models.Model):
    """ Post model. """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = CloudinaryField('image')
    #photo = models.ImageField(upload_to='posts/photos')
    likes = models.ManyToManyField(User, related_name="posts")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)


class Comment(models.Model):
    """ Post Comments """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    