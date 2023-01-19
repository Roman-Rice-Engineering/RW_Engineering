from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import WeeklyBlogPost

def blog(request):
    if request.method == "POST":
        if request.POST.get('delete_blog') and request.user.is_superuser:
            blog = WeeklyBlogPost.objects.get(id = request.POST.get('delete_blog'))
            blog.deleted = True
            blog.save()
        return HttpResponseRedirect('/blog')
    BlogClass = WeeklyBlogPost.objects.all()
    return render(request, 'blog/blog.html', {'AllBlogs': BlogClass})

def blog_post(request, id):
    if not WeeklyBlogPost.objects.filter(id = id).exists():
        raise Http404()
    blog = WeeklyBlogPost.objects.get(id = id)
    return render(request, 'blog/blog_post.html', {'blog': blog})

def blog_create(request):
    if not request.user.is_superuser:
        raise Http404()
    if request.method == "POST":
        print(request.POST)
    return render(request, 'blog/blog_create.html', {})