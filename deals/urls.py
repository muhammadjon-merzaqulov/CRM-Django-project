from django.urls import path
from . import views

urlpatterns = [
    path('', views.deal_list, name='deal_list'),
    path('<int:pk>/', views.deal_detail, name='deal_detail'),
    path('create/', views.deal_create, name='deal_create'),
    path('<int:pk>/update/', views.deal_update, name='deal_update'),
    path('<int:pk>/delete/', views.deal_delete, name='deal_delete'),
    path('update-stage/', views.update_deal_stage, name='update_deal_stage'),
]