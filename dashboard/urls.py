from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('<str:app_label>/<str:model_name>/', views.model_list, name='model_list'),
    path('<str:app_label>/<str:model_name>/add/', views.model_add, name='model_add'),
    path('<str:app_label>/<str:model_name>/<int:pk>/edit/', views.model_edit, name='model_edit'),
    path('<str:app_label>/<str:model_name>/<int:pk>/delete/', views.model_delete, name='model_delete'),
]
