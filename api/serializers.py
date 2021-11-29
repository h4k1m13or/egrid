from rest_framework import serializers

from main.models import PLNT, State


class PLNTSerializer(serializers.ModelSerializer):
    class Meta:
        model = PLNT
        fields = '__all__'


class STSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        exclude = ['geometry']
