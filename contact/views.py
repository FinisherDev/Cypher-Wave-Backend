from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact

# Create your views here.

class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        msg = 'Message From: ' + self.request.data['email'] + '\n Details: ' + self.request.data['message']
        send_mail("Customer Message", message=msg ,from_email=settings.EMAIL_HOST_USER, recipient_list=['Cypherwave66@gmail.com'])
        return super().perform_create(serializer)