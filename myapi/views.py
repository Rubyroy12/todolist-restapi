from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import HeroSereializer
from .models import Hero 
# Create your views here

class HeroList(APIView): #ModelViewSet  handles the GET and POST requests for our models
  def get(self, request,format=None):
      queryset = Hero.objects.all()
      serializers= HeroSereializer(queryset, many=True)
      return Response(serializers.data)

def home(request):
    return render(request,'home.html')


