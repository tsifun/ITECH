from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
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
     slug = models.SlugField()
>>>>>>> 9792bf7070101d72b8fa1095987834bacc148344
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad
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
