"""netfix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from . import views as v

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),

    # Main app (landing page, home, etc.)
    path('', include('main.urls')),

    # Services app
    path('services/', include('services.urls')),

    # User registration and login
    path('register/', include('users.urls')),  # Can be mapped to user registration views
    path('login/', include('users.urls')),     # Can be mapped to user login views

    # Profile and company views
    path('customer/<slug:name>/', v.customer_profile, name='customer_profile'),
    path('company/<slug:name>/', v.company_profile, name='company_profile'),
    path('companies/', v.company_list, name='company_list'),  # Adjusted for clarity
]