from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db import connection
import jwt
from django.conf import settings
from api.serializers.users_serializers import LoginSerializer

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = self.authenticate(email, password)
            if user:
                token = jwt.encode({'id': user['id']}, settings.SECRET_KEY, algorithm='HS256')
                return Response({'token': token}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def authenticate(self, email, password):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM authenticate_user(%s, %s)', [email, password])
            user = cursor.fetchone()
            if user:
                return {
                    'id': user[0],
                    'email': user[1]
                }
        return None