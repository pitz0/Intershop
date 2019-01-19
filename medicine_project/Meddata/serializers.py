from rest_framework import serializers
from .models import medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicine
        fields = ("ItemCode", "Descr")