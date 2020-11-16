from django.db import models
from django.db.models import Count

# Create your models here.

class Book1(models.Model):
    book_name = models.CharField(max_length=255, verbose_name='Book Name')
    description = models.CharField(max_length=255, verbose_name='Book Description')

    def __str__(self):
        return str(self.book_name)

class Topic(models.Model):
    topic_name = models.CharField(max_length=255, verbose_name='Subject Name')
    description = models.CharField(max_length=255, verbose_name='Topic Description')
    book = models.ForeignKey(Book1, verbose_name='book fk', related_name='topics',
                                related_query_name='topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name


class Post(models.Model):
    heading = models.CharField(max_length=255)
    content = models.TextField()
    topic = models.ForeignKey(Topic, verbose_name='topic fk', related_name='posts',
                              related_query_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return self.heading

