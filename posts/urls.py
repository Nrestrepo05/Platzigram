from django.urls import path

from posts import views 

urlpatterns = [

    path(
        route='',
        view=views.ListPostsView.as_view(),
        name='feed'
        ),

    path(
        route='new/',
        view=views.CreatePostView.as_view(),
        name='create_post'
        ),

    path(
        route='<int:pk>',
        view=views.PostDetailView.as_view(),
        name='post_detail'
    ),

]
