from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home_dark,name="home-dark"),
    path('home',views.index,name="index"),
    path('course',views.course,name="course"),
    path('course-Carousel',views.course_carousel,name="course-carousel"),
]