# api/urls.py
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import PostView
from board import views

router = DefaultRouter()
router.register("posts", views.PostView)

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list',
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/<int:pk>/comments/', views.CommentList.as_view()),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/',views.CommentDetail.as_view()),
])
