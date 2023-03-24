from django.db import models

# Create your models here.


class Contact(models.Model):
    contact_name = models.CharField(max_length=264)
    phone_number = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
    subject = models.CharField(max_length=264)
    message = models.CharField(max_length=464)

    def __str__(self):
        return self.contact_name


class PreviousWork(models.Model):
    project_name = models.CharField(max_length=128, null=True)
    img_url = models.ImageField(
        null=True, upload_to='images/', default='images/default.jpg')
    date = models.DateField(null=True)
    url = models.URLField(max_length=128, null=True)
    status = models.CharField(max_length=264, unique=True, null=True)

    def __str__(self):
        return str(self.project_name)
