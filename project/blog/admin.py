from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_time', 'view_times', )
    exclude = ('author', 'view_times', 'excerpt', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
