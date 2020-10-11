from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    heading=models.CharField(max_length=60,default="")
    category=models.CharField(max_length=50,default="")
    content=models.CharField(max_length=800,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title

# Create your models here.
