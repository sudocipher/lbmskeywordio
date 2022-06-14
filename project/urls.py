
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth

urlpatterns = [    
    path('admin/', admin.site.urls),
    # user related path
    path('', include('user.urls')),
    
]
