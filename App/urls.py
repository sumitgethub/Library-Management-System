from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('Book.urls')),
    path('user/', include('User.urls')),
]
