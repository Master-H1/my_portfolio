"""
URL configuration for merabu_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# Error handling
from django.conf.urls import handler404,handler403,handler500
from portfolio.views import custom_403_view,custom_404,custom_500
# ==========
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_honeypot.urls')),
    path('master/', admin.site.urls),
    path('',include('portfolio.urls'))
] 
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

# HTTP Error 403 - Forbidden
handler403 = custom_403_view

# Page not found
handler404 = custom_404

# Server Internal Error
handler500 = custom_500