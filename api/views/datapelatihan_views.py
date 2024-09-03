from rest_framework import generics, permissions, status
from api.models.datapelatihan_models import DataPelatihan
from api.serializers.datapelatihan_serializers import DataPelatihanSerializer
from api.models.pelatihanku_models import PelatihanKu
from api.serializers.pelatihanku_serializers import PelatihanKuSerializer

class DataPelatihanListCreateAPIView(generics.ListCreateAPIView):
    queryset = DataPelatihan.objects.all()
    serializer_class = DataPelatihanSerializer

class IsUserWithRole3(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_role == 3

class PurchaseDataPelatihanAPIView(generics.CreateAPIView):
    serializer_class = PelatihanKuSerializer
    permission_classes = [IsUserWithRole3]

    def create(self, request, *args, **kwargs):
        pelatihan_id = request.data.get('pelatihan_id')
        user = request.user
        pelatihan = DataPelatihan.objects.get(id=pelatihan_id)
        pelatihanku = PelatihanKu.objects.create(user=user, pelatihan=pelatihan)
        serializer = self.get_serializer(pelatihanku)
        return Response(serializer.data, status=status.HTTP_201_CREATED)