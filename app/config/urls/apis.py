from django.urls import path

from members import apis

urlpatterns = [
    path('members/', apis.UserList.as_view()),
    path('signup/', apis.SignUp.as_view()),

]
