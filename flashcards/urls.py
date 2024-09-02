from django.urls import path , include
from . import views


urlpatterns = [
    path('card-list', views.cardList, name='card-list'),
    path('card-detail/<str:pk>/', views.cardDetail, name='card-detail'),
    path('card-create/', views.cardCreate, name='card-create'),
    path('card-update/<str:pk>', views.cardUpdate, name='card-update'),
    path('card-delete/<str:pk>', views.cardDelete, name='card-delete'),
]