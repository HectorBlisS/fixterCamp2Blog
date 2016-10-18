from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Post
from .forms import PostForm



class Hola(View):
	def get(self,request):
		return render(request,'home.html')


class Listado(View):
	def get(self, request):
		posts = Post.objects.all()
		form = PostForm()
		context = {
		'posts':posts,
		'form':form
		}
		return render(request,'blog.html',context)



