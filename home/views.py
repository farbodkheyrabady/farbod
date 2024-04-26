from django.shortcuts import render
from blog.models import Blog

def home(request):
    q = Blog.objects.all()
    return render(request, "index.html", {"a":q})
