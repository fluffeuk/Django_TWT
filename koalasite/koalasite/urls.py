"""
URL configuration for koalasite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls"))
]


'''
TRIMMER

So what happens is url patterns calls path, with the first parameter being the first part of the path.
If it is admin, it will clip off admin from the start of the path and pass the next, remaining part 
to the next path in admin.site.urls.

## For example:
[ip]/admin/home will clip off the start, and pass 'home' to the next file. There, it will be checked if there is a 
home path, and if there is, it will take us there.

If it is blank (''), it will clip off only the ip from the start (essentially doing nothing) and pass the remaining part
to main.urls, where it will check

## For example:
[ip]/index/ will clip off the ip, and 'index/' will be passed on. If there is a path named index, it will take us there.



'''