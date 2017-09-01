from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Ad,Article,Catagory

# Create your views here.
def index0(request):
    return render(request, "blog/index_bak.html")

def index(request):
    ad_list = Ad.objects.all()
    blog_list = Article.objects.all()
    cata_list = Catagory.objects.all()
    context = {"ad_list": ad_list, "blog_list": blog_list, "cata_list":cata_list}
    return render(request, "blog/index.html", context)