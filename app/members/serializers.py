from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'img_profile',
            'introduce',
            'phone_number',
            'email',
            'main_position',
            'second_position',
        )

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password,
                                request=self.context.get('request'))
            if not user:
                raise serializers.ValidationError('자격인증정보가 올바르지 않습니다')
        else:
            raise serializers.ValidationError('이메일과 비밀번호를 입력해주세요')

        attrs['user'] = user
        return attrs