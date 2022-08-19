from django.db import models
from django.utils.timezone import now
from realtors.models import Realter
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HouseType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE ='Townhouse'

    realtor = models.ForeignKey(Realter, on_delete=models.DO_NOTHING)
    slug = models.CharField(_("Slug"), max_length=200,unique=True)
    title = models.CharField(_("Title"), max_length=150)
    address = models.TextField(_("Address"))
    city = models.CharField(_("City"), max_length=50)
    state = models.CharField(_("State"), max_length=50)
    zipcode = models.CharField(_("Zipcode"), max_length=50)
    description =models.TextField(_("Description"))
    sale_type = models.CharField(_("Sale Type"), choices=SaleType.choices, default=SaleType.FOR_SALE,max_length=20)
    price = models.IntegerField(_("Price"))
    bedrooms = models.IntegerField(_("Bed Rooms"))
    bathrooms = models.DecimalField(_("Bath Rooms"), max_digits=5, decimal_places=1)
    home_type = models.CharField(_("Home Type"), choices=HouseType.choices, default=HouseType.HOUSE,max_length=20)
    sqft = models.IntegerField(_("Sqft"))
    open_house = models.BooleanField(_("Open House"),default=False)
    photo_main = models.ImageField(_("Main Product Image"), upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_2 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_3 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_4 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_5 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_6 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_7 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_8 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_9 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_10 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_11 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_12 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_13 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_14 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_15 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_16 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_17 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_18 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_19 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    photo_20 = models.ImageField(_("More Product Image"), upload_to='photos/%Y/%m/%d',blank=True)
    is_published = models.BooleanField(_("Is Published"),default=True)
    list_date = models.DateTimeField(default=now,blank=True)

    def __str__(self):
        return self.title




