from django.shortcuts import render
from rest_framework import permissions
from .models import Contact
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response

# Create your views here.

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        data = self.request.data

        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                +'\nEmail: '
                +data['email']
                + '\n\nMessage: \n'
                + data['message'],
                'hasanakash799@gmail.com',
                ['hasanakash799@gmail.com'],
                fail_silently=False
            )
            contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            contact.save()
            return Response({'success': 'Message send successfully'})
        except:
            return Response({'error': 'Message Failed to send'})