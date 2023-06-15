from django.db import models


class JobOffer(models.Model):

    job_title = models.CharField(max_length=100, blank=False, null=False)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    posted_time = models.DateTimeField()
    experience = models.CharField(max_length=100)
    position_type = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField()

