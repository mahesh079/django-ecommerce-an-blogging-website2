from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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

class Blogcomment(models.Model):
	sno=models.AutoField(primary_key=True)
	comment=models.TextField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(Blogpost,on_delete=models.CASCADE)
	parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
	timesstamp=models.DateField(default=now)

	def __str__(self):
		return self.comment[0:15] + "..." +"By " + self.user.username
		