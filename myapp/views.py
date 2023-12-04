from django.shortcuts import render
from myapp import models
from account import models as account_models
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from myapp import serializers
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return render(request, 'myapp/index.html')

def services(request):
    services = models.Service.objects.all()
    return render(request, 'myapp/services.html', {'services': services})

def services_show(request, id):
    service = models.Service.objects.filter(id = id).first()
    doctors_group = Group.objects.get(name='doctors')
    doctors = account_models.CustomUser.objects.filter(groups=doctors_group)
    return render(request, 'myapp/service_index.html', {'service': service, 'doctors': doctors})

def about_us(request):
    return render(request, 'myapp/index.html')

def order(request):
    return render(request, 'myapp/order.html')

@api_view(['GET'])
def doctor_schedule(request, id):
    schedules = models.DoctorsSchedule.objects.filter(doctor__id = id)
    serializer = serializers.ScheduleSerializer(data = schedules, many = True)
    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)