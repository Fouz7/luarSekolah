from rest_framework import serializers
from api.models.pelatihanku_models import PelatihanKu

class PelatihanKuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PelatihanKu
        fields = '__all__'