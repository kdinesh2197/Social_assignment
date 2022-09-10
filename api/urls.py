from django.urls import path
from .views import user_profile, follow, Post, like, unlike, user_posts
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'post', Post)

urlpatterns = [
    path('user/', user_profile),
    path('follow', follow),
    path('like', like),
    path('unlike', unlike),
    path('all_posts', user_posts),
]
urlpatterns += router.urls
