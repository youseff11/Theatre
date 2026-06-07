from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'), 
    path('offers/', views.offers_view, name='offers'), 
    path('gallery/', views.gallery_view, name='gallery'), 
    path('achievements/', views.achievements_view, name='achievements'), 
    path('teams/', views.teams_view, name='teams'), 

]