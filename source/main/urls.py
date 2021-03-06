"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from webapp.views import guest, guest_create, guest_update, guest_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guest, name='index'),
    path('guests', guest, name='guest'),
    path('guest', guest_create, name='guest_add'),
    path('guest/<int:pk>/edit/', guest_update, name='guest_update'),
    path('guest/<int:pk>/delete/', guest_delete, name='guest_delete')

]