from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from User.models import User
from User.serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from User.utils import get_custom_jwt_token
from rest_framework import exceptions
from django.contrib.auth import authenticate



#user register api
class UserRegistrationView(APIView):


    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            User = serializer.save()
            token = get_custom_jwt_token(User)
            return Response({'token': token, 'msg': 'Registration Success'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user login api
class UserLoginView(APIView):


    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed(f'email {email} not register with library')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect Password')
        token = get_custom_jwt_token(user)
        return Response({'token': token, 'msg': 'login Success'}, status=status.HTTP_201_CREATED)







