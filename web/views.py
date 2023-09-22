from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,("index.html"))

def course(request):
    return render(request,("details/course.html"))

def course_carousel(request):
    return render(request,("details/course-carousel.html"))

def home_dark(request):
    return render(request,("details/index-dark.html"))