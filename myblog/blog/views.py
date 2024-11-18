from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

# Homepage view to list posts
def post_list(request):
    posts = Post.objects.all().order_by('-created')  # Fetch posts ordered by creation date
    return render(request, 'blog/post_list.html', {'posts': posts})

# Detail view for a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch post by primary key or return 404
    return render(request, 'blog/post_detail.html', {'post': post})