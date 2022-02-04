from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.contrib.auth.decorators import login_required



def blog(request):
    blogs = Blog.objects
    return render(request, 'blog/blog.html', {'blog':blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})

@login_required
def upload(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            blogs = Blog()
            blogs.title = request.POST['title']
            blogs.body = request.POST.get('body')
            blogs.image = request.FILES.get('image')
            blogs.pub_date = timezone.datetime.now()
            blogs.author = request.user
            blogs.save()
            return redirect('blog')
        else:
            return render(request, 'blog/upload.html', {'error': 'please enter all fields'})
    else:
        return render(request, 'blog/upload.html')