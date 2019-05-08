"""webhr URL Configuration

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
from cvranker import views
from django.contrib.admin.views.decorators import staff_member_required




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', staff_member_required(views.ApiView.as_view()), name='api view'),
    path('', views.add_cv, name= 'Homepage'),
    path('ranks', views.get_top_cvs, name='Ranks'),
    path('generate', views.GenerateScoredCvView.as_view(), name='generate'),
]