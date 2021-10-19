from django.db import models

# Create your models here.
class CategoryModel(models.Model):
	name=models.CharField(max_length=250 , null=False)
	slug=models.CharField(max_length=250 , null=False)
	def __str__(self):
		return self.name
class NewsModel(models.Model):
	title=models.CharField(max_length=250 , null=False)
	text=models.TextField()
	ctg=models.ForeignKey(CategoryModel , on_delete=models.CASCADE)	
	rasm=models.ImageField(upload_to='image/' , blank=True)
	time=models.DateTimeField(auto_now_add=True)	
	def __str__(self):
		return self.title
class UserModel(models.Model):
	email=models.EmailField()		
	def __str__(self):
		return self.email