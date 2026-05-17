from django.urls import include, re_path
import MyApp1.views
from django.contrib import admin
from django.urls import path
import account
from django.conf import settings
from django.conf.urls.static import static
"""
InClassDjangoLine6 URL Configuration

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

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path

urlpatterns = [
    path('admin', admin.site.urls),
    path('account', include('account.urls')),
    # Uncomment the next line to enable the admin:
    path('', MyApp1.views.index, name='index'),
    path('home', MyApp1.views.home, name ='home'),
    path('input', MyApp1.views.input_view, name='input'),
    path('register', account.views.register_view, name='register'),
    path('upload', MyApp1.views.upload_file, name='upload'),
    path('report/', MyApp1.views.report, name="report"),
    path('about', MyApp1.views.about_view, name="about"),
    path('category/<int:id>/', MyApp1.views.category_view, name='category'),
    path('delete/<int:id>/', MyApp1.views.delete_file, name='delete_file'),
    path('edit/<int:id>/', MyApp1.views.edit_file, name='edit_file'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


