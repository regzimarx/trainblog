from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
	posts_list = Blog.objects.all()
	return_data = {'posts': posts_list}
	return render(request, 'blog/index.html', return_data)