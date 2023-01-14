from django.contrib import admin
from .models import WeeklyBlogPost, Content, Text, Code_S, Code_M, Code_L, Image

admin.site.register(WeeklyBlogPost)
admin.site.register(Content)
admin.site.register(Text)
admin.site.register(Code_S)
admin.site.register(Code_M)
admin.site.register(Code_L)
admin.site.register(Image)