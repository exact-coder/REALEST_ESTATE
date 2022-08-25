from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=250)
    message = models.TextField(_("Message"),blank=True)
    contact_date= models.DateTimeField(_("Contact Time"), default=datetime.now, blank=True)

    def __str__(self) :
        return self.email
