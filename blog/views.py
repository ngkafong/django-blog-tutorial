from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView, DetailView, CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # template_name = <app>/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # template_name = <app>/<model>_form.html
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
