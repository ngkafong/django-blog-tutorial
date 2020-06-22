from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Richard',
        'title': 'BlogPost 1',
        'content': 'First post content',
        'date_posted': 'June 21, 2020'
    },
    {
        'author': 'RichardN',
        'title': 'BlogPost 2',
        'content': 'Second post content',
        'date_posted': 'June 21, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }

    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
