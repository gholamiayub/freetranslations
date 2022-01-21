from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('martor/', include('martor.urls')),
    path('user/', include('profile.urls')),
]
