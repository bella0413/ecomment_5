from django.urls import path

from . import views
from .views import PostList, PostDelete, PostCreate, PostUpdate, PostDetail, PostLike, PostUnlike, PostFavorite, PostFavoriteList,CategoryView

app_name = 'community'

urlpatterns = [
    path("", PostList.as_view(), name="index"),
    path("list/",PostList.as_view(), name='list'),
    path("create/",PostCreate.as_view(), name ='create'),
    path("delete/<int:pk>/",PostDelete.as_view(), name = 'delete'),
    path("update/<int:pk>/",PostUpdate.as_view(), name = 'update'),
    path("detail/<int:pk>/",PostDetail.as_view(), name = 'detail'),

    path("like/<int:post_id>/",PostLike.as_view(), name='like'),
    path("unlike/<int:post_id>/",PostUnlike.as_view(), name='unlike'),
    path("favorite/<int:post_id>/",PostFavorite.as_view(), name='favorite'),

    path("favorite_list/",PostFavoriteList.as_view(), name='favorite_list'),

    path('category/<str:cats>/',CategoryView, name='category'),

    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]



# 이미지 url 확실히 설정해서 사진 오류 없앰
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)