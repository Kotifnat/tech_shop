from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model()


class SignupView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, format=None):
        data = request.data

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            elif len(password) < 6:
                return Response({'error': 'Password must be at least 6 characters'})
            else:
                user = User.objects.create_user(email=email, name=name, password=password)
                user.save()
                return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})
