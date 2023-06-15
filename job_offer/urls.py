from django.urls import path
from job_offer import views

urlpatterns = [

    path('offers/', views.job_offer_list, name='offer_list'),
    #path('offers/',views.job_offer_detail, name='offer_detail')

]