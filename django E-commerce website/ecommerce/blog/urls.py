from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogHome"),
    path("blogpost/",views.blogpost,name="blogpost"),
    path("contact/",views.contact,name="contact"),
    path("search/",views.search,name="search"),
    path("aboutus/",views.aboutus,name="aboutus")
]
