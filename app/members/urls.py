from django.urls import path

from members import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]