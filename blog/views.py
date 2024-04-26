from django.shortcuts import render
from .models import Blog,Cate

def blog_list(request):
    a = Blog.objects.all()
    return render(request, "blog_list.html",context={"all":a})


def blog_det(request, id):
    w = Blog.objects.get(id=id)
    return render(request, "blog_det.html", {"b":w})


def category(request, pk):
    g = Cate.objects.get(id=pk)
    cd = g.cate.all()
    return render(request, "blog_list.html", {"all":cd})
