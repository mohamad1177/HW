from django.db import models


class Message(models.Model):
    """
    Represents a single blog post
    """
    created_date = models.DateTimeField(verbose_name='date of create', auto_now_add=True)
    creator = models.CharField(max_length=100, verbose_name='creator')
    content = models.TextField(verbose_name='content', null=True)
    title = models.CharField(max_length=100, verbose_name='title')
    email = models.CharField(max_length=100, verbose_name='email')
