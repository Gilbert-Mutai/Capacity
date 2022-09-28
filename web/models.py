from traceback import StackSummary
from django.db import models

# Create your models here.


class Testimonial(models.Model):
    image = models.ImageField(null=True, default="avatar.svg")
    comment = models.TextField(null=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, blank=True)
    job= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Faqs(models.Model):
    question = models.TextField(null=True, blank=True, max_length=255)
    answer = models.TextField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.question


class Contact(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    phone= models.CharField(max_length=255)
    message= models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.f_name
    

