import json

from django.contrib.auth import get_user_model

from config.settings.production import secrets

User = get_user_model()


class KakaoBackend:
    def authenticate(self, request, code):

        def get_access_token(code):
            url = 'https://kauth.kakao.com/oauth/token'
            params = {
                'grant_type': 'authorization_code',
                'client_id': secrets["KAKAO_REST_API_KEY"],
                'redirect_uri': 'http://localhost:8000/members/kakao_oauth/',
                'code': code,
            }
            response = request.get(url, params)
            response_dict = json.loads(response.text)
            access_token = response_dict['access_token']
            return access_token

        access_token = get_access_token(code)
        return access_token

