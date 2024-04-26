from django.db import models


class Cate(models.Model):
    title = models.CharField(max_length=20)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    cate = models.ManyToManyField(to=Cate,related_name="cate",null=True,blank=True)
    title = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    desc = models.TextField()
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    image = models.ImageField(blank=True, null=True, upload_to="post")

    def __str__(self):
        return self.title
