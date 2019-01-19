from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
def home(request):
	obj = Profile.objects
	return render(request,'profilede/index.html',{'obj':obj})
