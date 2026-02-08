from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Category, Heading
from .serializers import PostSerializer, PostListSerializer, CategorySerializer, HeadingSerializer

# Create your views here.


class PostListView(ListAPIView):
    queryset = Post.postObjects.all()  # Use the custom manager to get only published posts
    serializer_class = PostListSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.postObjects.all()  # Use the custom manager to get only published posts
    serializer_class = PostSerializer
    lookup_field = 'slug'  # Use slug for lookup instead of the default 'pk'