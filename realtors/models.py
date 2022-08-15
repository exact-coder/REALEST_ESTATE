from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Realter(models.Model):
    name = models.CharField(_("Realter Name"), max_length=50)
    photo = models.ImageField(_("Image"), upload_to='photos/%Y/%m/%d/')
    description = models.TextField(_("Details"),blank=True)
    phone = models.CharField(_("Phone Num"), max_length=20)
    email = models.CharField(_("Realter Email"), max_length=50)
    top_seller = models.BooleanField(_("Top Seller Status"),default=False)
    date_hired = models.DateTimeField(_("Hired Date"),default=datetime.now,blank=True)

    def __str__(self):
        return self.name
