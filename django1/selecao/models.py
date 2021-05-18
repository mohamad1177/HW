from datetime import datetime

from django.db import models


class Message(models.Model):
    """
    Represents a s
    """
    created_date = models.DateTimeField(verbose_name='date of create', auto_now_add=True)
    creator = models.CharField(max_length=100, verbose_name='creator')
    content = models.TextField(verbose_name='content', null=True)
    title = models.CharField(max_length=100, verbose_name='title')
    email = models.CharField(max_length=100, verbose_name='email', null=True)


class Post(models.Model):
    """
    Represents a single blog post
    """
    created_date = models.DateTimeField(verbose_name='created date', auto_now_add=True)
    creator = models.ForeignKey('auth.User', verbose_name='creator', on_delete=models.PROTECT)
    content = models.TextField(verbose_name='content', null=True)
    title = models.CharField(max_length=100, verbose_name='title')
    intro_image = models.ImageField(verbose_name='intro image', blank=True, null=True)
    show_post = models.BooleanField(verbose_name='show post', blank=True, null=True)


    class Meta:
        ordering = ('title',)
        verbose_name ='post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.title}'