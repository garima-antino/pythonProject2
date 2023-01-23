from django.db import models



class Article(models.Model):
    title = models.CharField(unique=True,max_length=200)
    description = models.CharField(max_length=500,null=True)
    published_at = models.DateTimeField()
    category = models.CharField(max_length=200,default='')
    country = models.CharField(max_length=100,default='')

