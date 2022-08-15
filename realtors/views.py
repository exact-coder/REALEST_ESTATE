from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realter
from .serializers import *

# Create your views here.

class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realter.objects.all()
    serializer_class =RealtorSerializer
    pagination_class = None

class RealtorView(RetrieveAPIView):
    queryset = Realter.objects.all()
    serializer_class = RealtorSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realter.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None