from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.db import connection

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.raw('SELECT * FROM get_users()')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        with connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO "user" (fullname, email, phone_number, password, confirm_password, user_role) VALUES (%s, %s, %s, %s, %s, %s)',
                [
                    serializer.validated_data['fullname'],
                    serializer.validated_data['email'],
                    serializer.validated_data['phone_number'],
                    serializer.validated_data['password'],
                    serializer.validated_data['confirm_password'],
                    serializer.validated_data['user_role']
                ]
            )