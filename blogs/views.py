from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog

def home(request):
	obj = Blog.objects.all
	# return HttpResponse('ok')
	return render(request,'blogs/home.html',{'obj':obj})

def det(request,blogid):
	obj=get_object_or_404(Blog,pk=blogid)
	return HttpResponse(obj.title)
