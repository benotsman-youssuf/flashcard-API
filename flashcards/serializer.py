from rest_framework import serializers
from .models import Flashcards

class FlashcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcards
        fields = '__all__'