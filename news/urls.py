from django.urls import path
from .views import ( 
    ArticleDelete, ArticleList, ArticleUpdate, PostList, 
    PostDetail, PostCreate, PostSearch, PostUpdate, 
    PostDelete, ArticleCreate, ArticleDetail
                    )


urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('article/', ArticleList.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article-delete'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article-update'),
]
