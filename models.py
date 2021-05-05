from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __repr__(self):
    #     rep = self.authors
    #     return rep

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(max_length=1000, default="A book")
    books = models.ManyToManyField(Books, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
