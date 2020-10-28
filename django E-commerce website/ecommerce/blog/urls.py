from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogHome"),
    path("blogpost/<int:id>",views.blogpost,name="blogpost"),
    path("search/",views.search,name="search"),
    path("aboutus/",views.aboutus,name="aboutus"),
    # api to post comment
    path('postComment',views.postComment,name="postComment")
]
