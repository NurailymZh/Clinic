from rest_framework import serializers
from . import models


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DoctorsSchedule
        fields = '__all__'