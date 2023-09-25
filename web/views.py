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
def blog(request):
    return render(request,("details/blog.html"))
def product(request):
    return render(request,("details/product.html"))
def team(request):
    return render(request,("details/team.html"))
def gallery(request):
    return render(request,("details/gallery.html"))
def contact(request):
    return render(request,("details/contact.html"))