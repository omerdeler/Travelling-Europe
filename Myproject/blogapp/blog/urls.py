from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index),
    path('blogs', views.blogs, name="blogs"),
    path('blogs_city', views.blogs_city, name="blogs_city"),
    path('category/<slug:slug>', views.blogs_by_category, name="blogs_by_category"),
    path('category_ulke/<slug:slug>', views.city_by_blog, name="city_by_blog"),
    path('category_city/<slug:slug>', views.trip_by_city, name="trip_by_city"),
    path('blogs/<slug:slug>', views.blogs_details, name="blogs_details"),
   


]