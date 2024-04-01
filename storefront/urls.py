"""
URL configuration for storefront project.

Mapping all apps URLs right after 127.0.0.1:8000/urlpattern
In urlpatterns below, any argument with --  include -- is routing to subpatterns from the app in the include argument. 

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# URL configuration:
urlpatterns = [
    path("admin/", admin.site.urls),
    # read the following like this: 
    # any URL that starts with 'playground/" should be ROUTED to the playground app"
    path('playground/', include('playground.urls)),
]
