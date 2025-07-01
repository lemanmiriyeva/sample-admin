from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),?
    path('admin/', include('dashboard.urls')),
     path('admin/', include('django.contrib.auth.urls')),
      path('admin/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
