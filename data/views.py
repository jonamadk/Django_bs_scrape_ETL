from django.db.models.query import QuerySet
from django.shortcuts import render
from .scrape import scrape_data
from .models import LiveTradingData
from .serializers import LiveTradingDataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication

from rest_framework import generics




# Create your views here.
class LiveTradingDataList(generics.ListCreateAPIView):
    
    queryset = LiveTradingData.objects.all()
    serializer_class = LiveTradingDataSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
  

    

  
class IndividualLiveTradingDataDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = LiveTradingData.objects.all()
    serializer_class = LiveTradingDataSerializer
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
  

