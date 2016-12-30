from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InstaUser, Post , Like, Comment, UserConnection
from .serializers import InstaUserSerializer, PostSerializer, LikeSerializer, CommentSerializer, UserConnectionSerializer
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.reverse import reverse
from profile_user.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # save the user object of the user that upload the post.
    def perform_create(self, serializer):
        try:
            user_var = self.request.user
            user_obj = InstaUser.objects.get(user=user_var)
            serializer.save(user=user_obj)
        except Exception as e:
            print(e)


# class InstaUserViewSet(viewsets.ReadOnlyModelViewSet):
class InstaUserViewSet(viewsets.ModelViewSet):
    queryset = InstaUser.objects.all()
    serializer_class = InstaUserSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        try:
            post_var = str(self.request.data['post_id'])
            user_var = self.request.user
            post_obj = Post.objects.get(id=post_var)
            user_obj = InstaUser.objects.get(user=user_var)
            if Like.objects.get(user=user_obj, post=post_obj) is None:
                serializer.save(user=user_obj, post=post_obj)
            else:
                raise ValueError
        except ValueError as e:
            return Response(data=e, status=404)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        try:
            post_var = str(self.request.data['post_id'])
            user_var = self.request.user
            post_obj = Post.objects.get(id=post_var)
            user_obj = InstaUser.objects.get(user=user_var)
            serializer.save(user=user_obj, post=post_obj)
        except Exception as e:
            print(e)


class UserConnectionViewSet(viewsets.ModelViewSet):
    queryset = UserConnection.objects.all()
    serializer_class = UserConnectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        try:
            user_followed_var = str(self.request.data['followed_user_id'])
            user_var = self.request.user
            user_followed_obj = InstaUser.objects.get(user=user_followed_var)
            user_obj = InstaUser.objects.get(user=user_var)
            serializer.save(user=user_obj, followed_user=user_followed_obj)
        except Exception as e:
            print(e)



@api_view(['GET','POST'])
def api_root(request, format=None):
    return Response({
        'instauser': reverse('instauser-list', request=request, format=format),
    })





# class PostViewSet(viewsets.ViewSet):
#     queryset = Post.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly,)
#
#     def list(self, request, instauser_pk=None):
#         queryset = self.queryset.filter(user=instauser_pk)
#         serializer = PostSerializer(queryset, many=True, context={'request': request})
#         return Response(data=serializer.data)
#
#
#     def retrieve(self, request, pk=None):
#         # try:
#             post = get_object_or_404(self.queryset, pk=pk)
#             serializer = PostSerializer(post, context={'request': request})
#             return Response(data=serializer.data)
#         # except Exception as e:
#         #     test =e
#
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
#
#
# class InstaUserViewSet(viewsets.ViewSet):
#     queryset = InstaUser.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly,)
#
#     def list(self, request):
#         queryset = InstaUser.objects.filter()
#         serializer = InstaUserSerializer(queryset, many=True, context={'request': request})
#         return Response(data=serializer.data, template_name='profile_user/users.html')
#
#     def retrieve(self, request, pk=None):
#         queryset = InstaUser.objects.filter()
#         isntausers = get_object_or_404(queryset, pk=pk)
#         serializer = InstaUserSerializer(isntausers, context={'request': request})
#         return Response(data=serializer.data)
#
# #
# #
# #
#



#----------------- sending HTML template as a response! -----------------------------------------


    # class InstaUserViewSet(viewsets.ViewSet):
    #     queryset = InstaUser.objects.all()
    #     renderer_classes = (TemplateHTMLRenderer,)
    #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                           IsOwnerOrReadOnly,)
    #
    #     def list(self, request):
    #         queryset = InstaUser.objects.filter()
    #         serializer = InstaUserSerializer(queryset, many=True, context={'request': request})
    #         return Response(data=serializer.data, template_name='profile_user/users.html')
    #
    #     def retrieve(self, request, pk=None):
    #         queryset = InstaUser.objects.filter()
    #         isntausers = get_object_or_404(queryset, pk=pk)
    #         serializer = InstaUserSerializer(isntausers, context={'request': request})
    #         return Response(data=serializer.data, template_name='profile_user/users.html')





# -------------------------------------------------------------
# class InstaUserList(generics.ListCreateAPIView):
#     queryset = InstaUser.objects.all()
#     serializer_class = InstaUserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#
# class InstaUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = InstaUser.objects.all()
#     serializer_class = InstaUserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#     # make sure the user that upload the post will be recognized with it.
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)
#


# ------------------
#
# class PostPicture(generics.GenericAPIView):
#     queryset = Post.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         post = self.get_object()
#         return Response(post.value)
#
#

# ------------
    #
    # class InstaUserViewSet(viewsets.ReadOnlyModelViewSet):
    #     """
    #     This viewset automatically provides `list` and `detail` actions.
    #     """
    #     queryset = InstaUser.objects.all()
    #     serializer_class = InstaUserSerializer
    #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                           IsOwnerOrReadOnly,)
    #
    # class PostViewSet(viewsets.ModelViewSet):
    #     """
    #     This viewset automatically provides `list`, `create`, `retrieve`,
    #     `update` and `destroy` actions.
    #     """
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer
    #     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                           IsOwnerOrReadOnly,)
    #
    #     def perform_create(self, serializer):
    #         serializer.save(user=self.request.user)
    #






    # class InstaUserList(APIView):
#     def get(self, request, format=None):
#         insta_user = InstaUser.objects.all()
#         serializer = InstaUserSerializer(insta_user, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = InstaUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class insta_user_detail(APIView):
#     """
#     Retrieve, update or delete a InstaUser instance.
#     """
#     def get_object(self, pk):
#         try:
#             return InstaUser.objects.get(pk=pk)
#         except InstaUser.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         insta_user = self.get_object(pk)
#         serializer = InstaUserserializer(insta_user)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         insta_user = self.get_object(pk)
#         serializer = InstaUserserializer(insta_user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         insta_user = self.get_object(pk)
#         insta_user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)