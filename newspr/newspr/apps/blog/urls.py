from django.urls import path 
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',home_page,name='home_page'),
    path('list_posts/',ListPost.as_view(),name='list_posts'),
    path('list_post/<int:pk>/',DetailPost.as_view(),name='detail_post'),
    path('list_categorys/',ListCategorys.as_view(),name='list_cats'),
    path('list_post/<int:pk>/add_comment/',CommentAdd.as_view(),name='add_comment'),
    path('list_categorys/<str:slug>/',CategoryPosts.as_view(),name='category_posts')
]