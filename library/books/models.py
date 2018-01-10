from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    """Define book details and description."""

    title = models.CharField(max_length=500)
    author = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.URLField(max_length=400)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)


class Category(models.Model):
    """Define category description."""

    name = models.CharField(max_length=255)
