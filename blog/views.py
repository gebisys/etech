from django.shortcuts import render
from blog.models import Post

def index(request):
	list_post = Post.objects.all()
	return render(request, 'blog/list_post.html',{
		'list_post' : list_post,
	})

def view_post(request, slug, id):
	try:
		post = Post.objects.get(id = id, slug = slug)
	except Post.DoesNotExist:
		render(request, '404_blog.html')
	return render(request, 'blog/view_post.html', {
		'post' : post
	})