from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
>>>>>>> 494c4bd5839960f7c21e3ba2e673ddb51c4f95bb
class Category(models.Model):
     name = models.CharField(max_length=128, unique=True)
     views = models.IntegerField(default=0)
     likes = models.IntegerField(default=0)
<<<<<<< HEAD
     slug = models.SlugField(unique=True)
=======
<<<<<<< HEAD
     slug = models.SlugField(unique=True)
=======
<<<<<<< HEAD
     slug = models.SlugField(unique=True)
=======
     slug = models.SlugField()
>>>>>>> 9792bf7070101d72b8fa1095987834bacc148344
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad
>>>>>>> 494c4bd5839960f7c21e3ba2e673ddb51c4f95bb
     def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super(Category, self).save(*args, **kwargs)
     class Meta:
         verbose_name_plural = 'Categories'
     def __str__(self): # For Python 2, use __unicode__ too
             return self.name
class Page(models.Model):
     category = models.ForeignKey(Category)
     title = models.CharField(max_length=128)
     url = models.URLField()
     views = models.IntegerField(default=0)
     def __str__(self): # For Python 2, use __unicode__ too
        		return self.title
				
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
     user = models.OneToOneField(User)

    # The additional attributes we wish to include.
     website = models.URLField(blank=True)
     picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
     def __unicode__(self):
        return self.user.username