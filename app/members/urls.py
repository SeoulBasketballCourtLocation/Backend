from django.urls import path

from members import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('kakao_oauth/', views.kakao_oauth, name='kakao-oauth'),
]