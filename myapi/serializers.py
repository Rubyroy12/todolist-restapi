from .models import Hero
from rest_framework import fields, serializers


class HeroSereializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields= ('name','alias')
        