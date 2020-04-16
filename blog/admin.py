from django.contrib import admin
from .models import Post

admin.site.register(Post)
#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
    #list_display = ('title',  'author', 'published_date')
    #list_filter = ('created_date', 'published_date', 'author')
    #search_fields = ('title', 'text')
    #date_hierarchy = 'published_date'
