from django.contrib import admin

# Register your models here.
from .models import Blogpost,Blogcomment
admin.site.register((Blogpost,Blogcomment))