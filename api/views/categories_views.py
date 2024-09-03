from rest_framework import generics
from api.models.categories_models import Category
from api.serializers.categories_serializers import CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.raw('SELECT * FROM "category"')
    serializer_class = CategorySerializer