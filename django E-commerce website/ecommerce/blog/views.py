from django.shortcuts import render
from django.http import HttpResponse
# create your views here
# def index(request):
#     return HttpResponse("Index blog")
def index(request):
    return render(request,'blog/index.html')
def blogpost(request):
    return render(request,'blog/blogpost.html')
def contact(request):
    return render(request,'blog/contact.html')
def search(request):
    return render(request,'blog/search.html')
def aboutus(request):
    return render(request,'blog/aboutus.html')