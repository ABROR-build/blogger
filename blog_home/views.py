from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_home.html', context)

def detailed_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

class BlogCreateView(CreateView):
    model = Post
    template_name = 'NewPost.html'
    fields = ['title', 'summary', 'author', 'text']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'summary', 'text']
def about_page(request):
    return render(request, template_name='about.html')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirect to your login page or any other desired URL
    else:
        # Handle GET requests (optional)
        return render(request, 'logged_out.html')