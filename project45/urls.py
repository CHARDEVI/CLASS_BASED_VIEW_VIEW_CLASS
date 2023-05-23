"""project45 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cherry.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fb_views/',fb_views,name='fb_views'),
    path('cb_views/',cb_views.as_view(),name='cb_views'),
    path('cbv_context',cbv_context.as_view(),name='cbv_context'),
    path('HTML_FORM/',HTML_FORM.as_view(template_name='HTML_FORM.html'),name='HTML_FORM'),
    path('HTML_DIRECT/',TemplateView.as_view(template_name='HTML_DIRECT.html'),name='HTML_DIRECT'),
    path('CLASS_HTML/',CLASS_HTML.as_view(),name='CLASS_HTML'),





    




]
