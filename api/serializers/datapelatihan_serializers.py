from rest_framework import serializers
from api.models.datapelatihan_models import DataPelatihan

class DataPelatihanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPelatihan
        fields = '__all__'