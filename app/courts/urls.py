from django.urls import path

from courts import views

urlpatterns = [
    path('', views.courts_list, name='courts-list'),
    path('<int:pk>/', views.court_detail, name='court-detail'),

]