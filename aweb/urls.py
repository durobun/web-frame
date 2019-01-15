"""aweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from blog import views as main_view

extra_patterns = [
    path('extra1/', main_view.get_extra1),
    path('extra2/', main_view.get_extra2),
]

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('rest_framework', include('rest_framework.urls')),
    path('path/', include('path.urls')),
    #path('repath/', include('repath.urls')),
    path('extra/', include(extra_patterns)),
    path('fbv/', include('fbv.urls')),
]
