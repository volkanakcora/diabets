from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import HeroSerializer
from .models import Hero
from diabet import ML
import pandas as pd
import numpy as np
from scripts import analyze_entry


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class HeroML(viewsets.ModelViewSet):

    serializer_class = HeroSerializer
    # user_input_age = # int(request.GET["Glucose", "insulin", "BMI", "Diabetesfunction", "Age"])
    # user_input = pd.DataFrame(user_input_age).T
    # prediction = ML.prediction(user_input)
    # print(prediction)  # render(request, 'result.html', {'prediction': prediction})

@api_view(['GET', 'POST'])
def handle_request(request):
    if request.method == 'GET':
        print('server is on')
        return Response(status=200)

    if request.method == 'POST':

        data = analyze_entry.prediction(request.data)
        serializer = HeroSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()


        return Response(status=201)