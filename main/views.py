from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
# Create your views here.


class HomeView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')[:2]
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')

        if tag:
            return Post.objects.filter(tags__name=tag)
        if category:
            return Post.objects.filter(category__name=category)
        if q:
            return Post.objects.filter(title__icontaince=q)


class AboutView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def about(self):
        extra_info = self.request.query_params.get('extra')

        if extra_info:
            return About.objects.filter(extra__name=extra_info)
