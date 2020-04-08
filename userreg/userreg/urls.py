
from django.contrib import admin
from django.urls import include, path
from .views import index, logout_view, some

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',index),
    path('accounts/logout',logout_view),
    path('',some),
   
]
