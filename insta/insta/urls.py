"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from profile_user import views as profile_user_view
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from rest_framework_nested import routers as nested_routers
from django.contrib import admin
from rest_framework import routers

router = nested_routers.DefaultRouter()
router.register(r'instausers', profile_user_view.InstaUserViewSet)
router.register(r'posts', profile_user_view.PostViewSet)
router.register(r'likes', profile_user_view.LikeViewSet)
router.register(r'comments', profile_user_view.CommentViewSet)
router.register(r'userconnections', profile_user_view.UserConnectionViewSet)


# router = nested_routers.SimpleRouter()
# posts_router = nested_routers.N;  שסestedSimpleRouter(router, r'instausers', lookup='instauser')
# posts_router.register(r'posts', profile_user_view.PostViewSet, base_name='instauser-posts')



urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^', include(posts_router.urls)),
    url(r'^$', profile_user_view.api_root),
    # include the login and logout views for the browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
            ]



#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)























