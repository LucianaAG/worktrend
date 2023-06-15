from django.shortcuts import render
from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view
from job_offer.models import JobOffer
from job_offer.serializers import JobOfferSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def job_offer_list(request):
    
    if request.method == 'GET':
        job_offer = JobOffer.objects.all()
        serializer = JobOfferSerializer(job_offer, many=True)
        return response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
         serializer = JobOfferSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_200_OK)
    return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_offer_detail(request, pk):

    job_offer = JobOffer.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = JobOfferSerializer(job_offer)
        return response(serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == 'PUT':
        serializer = JobOfferSerializer(job_offer, data = request.data)  
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_200_OK)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        job_offer.delete()
        return response('{}', status=status.HTTP_204_NO_CONTENT)
