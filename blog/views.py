from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
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
        return HttpResponse('Error, blog post does not exist')
    blog = WeeklyBlogPost.objects.get(id = id)
    return render(request, 'blog/blog_post.html', {'blog': blog})