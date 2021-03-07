from django.contrib import admin

# Register your models here.
from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, PostAdmin)