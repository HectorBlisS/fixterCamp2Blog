from django.db import models



class Post(models.Model):
	titulo = models.CharField(max_length=140)
	desc = models.TextField(blank=True,null=True)
	autor = models.CharField(max_length=50,blank=True,null=True)
	categorias = models.CharField(max_length=140,blank=True,null=True)
	img = models.CharField(max_length=140,blank=True,null=True)
		
	def __str__(self):
		return self.titulo