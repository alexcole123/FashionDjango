from django.db import models
from rest_framework.serializers import ModelSerializer
from clothing.models import ClothingModel

class ClothingSerializer(ModelSerializer):

    class Meta:
        model = ClothingModel
        fields = "__all__" #all fields

