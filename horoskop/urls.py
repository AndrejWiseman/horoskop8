from django.urls import path
from .views import index, znak_detaljno

urlpatterns = [
    path('', index, name='index'),
    path('horoskop/<slug:slug>/', znak_detaljno, name='znak-detaljno'),

]