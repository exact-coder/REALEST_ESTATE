from rest_framework import serializers
from .models import Realter


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realter
        fields = '__all__'