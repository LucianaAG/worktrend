from django.contrib import admin
from job_offer.models import JobOffer

# Register your models here.

class JobOfferAdmin(admin.ModelAdmin):
    list_display = (
        'job_title', 
        'company', 
        'experience', 
        'location', 
        'location', 
        'source', 
        'posted_time', 
        'experience',
        'position_type', 
        'description', 
        'rating'
    )

admin.site.register(JobOffer, JobOfferAdmin)
