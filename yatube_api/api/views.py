from rest_framework import filters, viewsets
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
)
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Follow, Group, Post
from .permissions import AuthorIsOwnerOrReadOnly, IsOwner
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)

RAISE_MESSAGE = 'У вас недостаточно прав для выполнения данного действия.'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    pagination_class = LimitOffsetPagination
    permission_classes = [AuthorIsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AuthorIsOwnerOrReadOnly]

    def filter_queryset(self, queryset):
        post_pk = self.kwargs.get('post_pk')
        queryset = Comment.objects.filter(post_id=post_pk)
        return queryset

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('post_pk')
        serializer.save(author=self.request.user, post_id=post_pk)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('=following__username', '=user__username')

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
