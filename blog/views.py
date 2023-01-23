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
    if blog.deleted:
        raise Http404

    return render(request, 'blog/blog_post.html', {'blog': blog})

def blog_create(request):
    if not request.user.is_superuser:
        raise Http404()
    if request.method == "POST":
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
            code_sCounter = 0
            code_mCounter = 0
            code_lCounter = 0

            new_blog_post = WeeklyBlogPost()
            new_blog_post.title = title
            new_blog_post.thumbnail = thumbnail
            new_blog_post.thumbnail_description = thumbnail_description
            new_blog_post.save()
            
            for index_item in index:
                if index_item == "text":
                    new_content = new_blog_post.content_set.create(content_type = "text")
                    new_content.save()
                    new_content_field = new_content.text_set.create()
                    new_content_field.text = text[textCounter]
                    new_content_field.save()
                    textCounter += 1
                elif index_item == "image":
                    new_content = new_blog_post.content_set.create(content_type = "image")
                    new_content.save()
                    new_content_field = new_content.image_set.create()

                # Important note!!!! if image field is left blank the flollowing code may cause images to be placed in incorrect positions
                    if(imageCounter < len(image)):
                        new_content_field.image = image[imageCounter]

                    
                    new_content_field.image_description = image_description[imageCounter]
                    new_content_field.save()
                    imageCounter += 1
                if index_item == "code_s":
                    new_content = new_blog_post.content_set.create(content_type = "code_s")
                    new_content.save()
                    new_content_field = new_content.code_s_set.create()
                    new_content_field.code = code_s[code_sCounter]
                    new_content_field.save()
                    code_sCounter += 1
                if index_item == "code_m":
                    new_content = new_blog_post.content_set.create(content_type = "code_m")
                    new_content.save()
                    new_content_field = new_content.code_m_set.create()
                    new_content_field.code = code_m[code_mCounter]
                    new_content_field.save()
                    code_mCounter += 1
                if index_item == "code_l":
                    new_content = new_blog_post.content_set.create(content_type = "code_l")
                    new_content.save()
                    new_content_field = new_content.code_l_set.create()
                    new_content_field.code = code_l[code_lCounter]
                    new_content_field.save()
                    code_lCounter += 1

                new_blog_post.save()
    return render(request, 'blog/blog_create.html', {})