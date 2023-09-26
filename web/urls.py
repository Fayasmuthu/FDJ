from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home_dark,name="home-dark"),
    path('home',views.index,name="index"),
    path('course',views.course,name="course"),
    path('course',views.course_carousel,name="course-carousel"),
    path('blog',views.blog,name="blog"),
    path('gallery',views.gallery,name="gallery"),
    path('product',views.product,name="product"),
    path('team',views.team,name="team"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('Donate',views.donate,name="donate"),
    path('Cause',views.cause,name="cause"),
]