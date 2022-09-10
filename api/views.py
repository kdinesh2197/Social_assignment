from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comments, Follow,Posts
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework import viewsets

@api_view(['GET'])
def user_profile(request):
    user = request.user
    follower = Follow.objects.filter(author_id=user.id).count()
    following = Follow.objects.filter(follower_id=user.id).count()
    return Response({"User Name": f'{user.first_name} {user.last_name}', 'follower':follower,'following':following})


@api_view(['POST'])
def follow(request):
    author_id = request.POST.get('author')
    user = request.user
    following = Follow.objects.get_or_create(author_id=author_id,follower_id=user.id)
    return Response({"message": "You succuessfuly followed the given User"})

@api_view(['POST'])
def unfollow(request):
    author_id = request.POST.get('author')
    user = request.user
    following = Follow.objects.filter(author_id=author_id,follower_id=user.id)
    if following.exists():
        following.delete()
    return Response({"message": "You succuessfuly unfollowed the given User"})


class Post(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
        user = self.request.user
        title = self.request.POST.get('title')
        desc = self.request.POST.get('description')
        obj = Posts.objects.create(title=title, description=desc, user=user)
        return Response({'success':'success'})


@api_view(['POST'])
def like(request):
    id = request.POST.get('id')
    user = request.user
    post = Posts.objects.get(id=id)
    post.likes = post.likes+1
    post.save()
    return Response({"message": "You succuessfuly liked the given Post"})


@api_view(['POST'])
def unlike(request):
    id = request.POST.get('id')
    user = request.user
    post = Posts.objects.get(id=id)
    post.likes = post.likes-1
    post.save()
    return Response({"message": "You succuessfuly unliked the given Post"})

@api_view(['POST'])
def comment(request):
    id = request.POST.get('id')
    comment_test = request.POST.get('comment')
    user = request.user
    post = Posts.objects.get(id=id)
    comment= Comments.objects.create(commnet=comment_test)
    post.comments.add(comment)
    post.save()
    return Response({"message": "You succuessfuly added comment the given Post"})


@api_view(['GET'])
def user_posts(request):
    user = request.user
    posts = Posts.objects.filter(user=user)
    serializer = PostSerializer(posts, many=True)
    return Response({'data': serializer.data})