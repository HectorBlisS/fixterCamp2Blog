from django.shortcuts import render, HttpResponse, redirect
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

	def post(self,request):
		form = PostForm(request.POST)
		form.save()
		return redirect('lista')
		# context = {
		# # 'posts':posts,
		# 'form':form
		# }
		# return render(request,'blog.html',context)


