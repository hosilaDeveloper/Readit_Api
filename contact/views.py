from django.shortcuts import render
from .models import Contact, ContactInfo
from .serializers import ContactSerializer, ContactInfoSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.


class ContactInfoView(ListAPIView):
    queryset = ContactInfo.objects.all().order_by('-id')[:1]
    serializer_class = ContactSerializer


class ContactView(CreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
