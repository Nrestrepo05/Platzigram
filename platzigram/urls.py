from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    
    # Posts
    path('', include(('users.urls', 'users'), namespace='users')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
