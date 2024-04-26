from blog.models import Blog,Cate

def blog(request):
    e = Blog.objects.order_by("-create")[:3]
    return {"recent":e}
def category(request):
    f = Cate.objects.all()
    return {"d":f}