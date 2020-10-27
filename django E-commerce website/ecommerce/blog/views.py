from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# create your views here
# def index(request):
#     return HttpResponse("Index blog")
def index(request):
    allblogs=[]
    test=Blogpost.objects.all()
    print(test)
    catblogs=Blogpost.objects.values('category','post_id')
    cats={post['category'] for post in catblogs}
    for cat in cats:
        cat1=Blogpost.objects.filter(category=cat)
        # n=len(cat1)
        allblogs.append(cat1)
    print(allblogs)
    params={'allblogs':allblogs}
    return render(request,'blog/index.html',params)
def blogpost(request,id):
    blog=Blogpost.objects.filter(post_id=id)
    return render(request,'blog/blogpost.html',{'blog':blog[0]})
def search(request):
    newblog=[]
    if request.method=='POST':
        blog2=request.POST.get('search','')
        if len(blog2)>0:
            blog=Blogpost.objects.values('category')
            # print(blog)
            new2={item3['category'] for item3 in blog}
            # for new3 in new2:
            blog3=Blogpost.objects.filter(category=blog2)
            # print("This is blog3:",blog3)
            # product2=Product.objects.all()
            n=len(blog3)
            newblog.append(blog3)
            params2={'newblog':newblog,'blog2':blog2 }
            # print("this is product",product)
            # print("this is newprods",newprods)
            # print("this is product2",product2)
            if len(blog3)==0:
                return HttpResponse('Blog not found')
            else:
                return render(request,"blog/search.html",params2)

    allblogs=[]
    catprods=Blogpost.objects.values('category','post_id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Blogpost.objects.filter(category=cat)
        n=len(prod)
        allblogs.append(prod)
    # allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allblogs':allblogs }
    return render(request,"blog/index.html", params)           
def aboutus(request):
    return render(request,'blog/aboutus.html')