from django.contrib import admin
from django.urls import path
from similarRect import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_name, name = 'Home'),
]
