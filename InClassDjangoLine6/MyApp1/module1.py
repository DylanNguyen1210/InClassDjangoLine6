from django.urls import include, path
from MyApp1 import views
    
    
    
urlspatterns = [
    path('', MyApp1.views.index, name='index'),
    path('about/', MyApp1.views.about, name='about'),
    path('contact/', MyApp1.views.contact, name='contact'),        
]
