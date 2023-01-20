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
        print(request.FILES)
        if index := request.POST.getlist("index"):
            title = request.POST.get("title")
            thumbnail = request.FILES.get("thumbnail")
            thumbnail_description = request.POST.get("thumbnail_description")
            text = request.POST.getlist("text")
            image = request.FILES.getlist("image")
            image_description = request.POST.getlist("image_description")
            code_s = request.POST.getlist("code_s")
            code_m = request.POST.getlist("code_m")
            code_l = request.POST.getlist("code_l")

            textCounter = 0
            imageCounter = 0
            image_descriptionCounter = 0
            code_sCounter = 0
            code_mCounter = 0
            code_lCounter = 0

            new_blog_post = WeeklyBlogPost()
            new_blog_post.save()
            for index_item in index:
                if index_item == "title":
                    new_blog_post.title = title
                elif index_item == "thumbnail":
                    new_blog_post.thumbnail = thumbnail
                    new_blog_post.thumbnail_description = thumbnail_description
                elif index_item == "text":
                    new_content = new_blog_post.content_set.create()
                    new_content.content_type = "text"
                    new_content.save()
                    new_content_field = new_content.text_set.create()
                    new_content_field.text = text[textCounter]
                    new_content_field.save()
                    textCounter += 1

                new_blog_post.save()
    return render(request, 'blog/blog_create.html', {})