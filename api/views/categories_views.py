from rest_framework import generics
from api.models.categories_models import Category
from api.serializers.categories_serializers import CategorySerializer

class CategoryListCreateAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer