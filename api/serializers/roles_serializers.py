from rest_framework import serializers
from api.models.roles_models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'