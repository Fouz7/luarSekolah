from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from api.models.pelatihanku_models import PelatihanKu
from api.serializers.pelatihanku_serializers import PelatihanKuSerializer

class IsUserWithRole3(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.user_role == 3

class PelatihanKuListAPIView(generics.ListAPIView):
    serializer_class = PelatihanKuSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsUserWithRole3]

    def get_queryset(self):
        return PelatihanKu.objects.filter(user=self.request.user)