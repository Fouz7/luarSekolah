from rest_framework import generics
from api.models.roles_models import Role
from api.serializers.roles_serializers import RoleSerializer

class RoleListAPIView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer