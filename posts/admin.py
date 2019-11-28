from django.contrib import admin
from .models import Post

@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'title', 'user', 'picture',)
    list_display_links = ('pk', 'title', 'user', 'picture')

    search_fields = ('user__first_name', 'user__last_name', 'title')
    list_filter = ('created', 'modified')


