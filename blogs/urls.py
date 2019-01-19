from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name="blog"),
	path('<int:blogid>/',views.det,name="details")
]
