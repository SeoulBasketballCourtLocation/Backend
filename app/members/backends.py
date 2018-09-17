import json
import requests
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
            response = requests.get(url, params)
            response_dict = json.loads(response.text)
            access_token = response_dict['access_token']
            return access_token

        def app_connection(access_token):
            url = 'https://kapi.kakao.com/v1/user/signup/'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            }
            response = requests.post(url, headers=headers)
            response_dict = response.json()
            return response_dict

        def get_profile(access_token):
            url = 'https://kapi.kakao.com/v2/user/me'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
                # 연령대와 생일을 알기 위해서는 kakao_account.age_range, kakao_account.birthday 추가
                'property_keys': '["properties.nickname", "kakao_account.email"]',
            }
            response = requests.post(url, headers=headers)
            response_dict = response.json()
            return response_dict

        def create_user_by_kakao(id, nickname, profile_image):
            kakao_id = id
            nickname = nickname
            profile_image = profile_image
            return User.objects.get_or_create(username=kakao_id, defaults = {
                'username':kakao_id,
                'img_profile':profile_image,
            })

        access_token = get_access_token(code)
        # app_connection(access_token)
        user_info_dict = get_profile(access_token)

        id = user_info_dict['id']
        nickname = user_info_dict['properties']['nickname']
        profile_image = user_info_dict['properties']['profile_image']
        user, new_user = create_user_by_kakao(id=id, nickname=nickname, profile_image=profile_image)

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None