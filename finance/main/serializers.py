from rest_framework import serializers
from main import models


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.OperationModel
