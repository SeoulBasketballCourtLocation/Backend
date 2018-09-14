from django.urls import path

from courts.apis import CourtList
from members.apis import UserList, SignUp, AuthToken, ProfileView

urlpatterns = [
    path('members/', UserList.as_view()),
    path('signup/', SignUp.as_view()),
    path('authtoken/', AuthToken.as_view()),
    path('profile/', ProfileView.as_view()),
    path('courts/', CourtList.as_view()),
]
