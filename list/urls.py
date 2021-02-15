from django.urls import path,include
from . import views
#from . import sessions

urlpatterns = [
    path('', views.home),
    path('update/<str:pk>/', views.update),
    path('delete/<str:pk>/', views.delete),
    path('stat/',views.stat),
    path('admi/',views.admi),
    path('admi/list/',views.list),
    path('adm/',include('django.contrib.auth.urls')),
   
  
]
