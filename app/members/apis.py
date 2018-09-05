from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializers import UserSerializer

User = get_user_model()

class UserList(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class SignUp(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(raw_password=request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthToken(APIView):
    def post(self, request):
        # 전달받은 데이터에서 username, password추출

        # email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate가 성공한 경우
        user = authenticate(username=username, password=password)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if user:
            # Token을 가져오거나 없으면 생성
            token, __ = Token.objects.get_or_create(user=user)
            # Response에 돌려줄 데이터
            user_info = serializer.validated_data['user']
            data = {
                'token':token.key,
                'user':UserSerializer(user_info).data
            }
            return Response(data)
        # authenticate에 실패한 경우
        raise AuthenticationFailed('인증정보가 올바르지 않습니다')