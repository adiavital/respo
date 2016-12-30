from rest_framework import serializers

from.models import InstaUser, Post , Comment, Like, UserConnection
from.user_connection_helper import user_connection_helper

class InstaUserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, queryset=Post.objects.all(), view_name="post-detail")
    # userconnections = serializers.HyperlinkedRelatedField(many=True, queryset=UserConnection.objects.all(), view_name="userconnection-detail")
    #     posts = serializers.HyperlinkedIdentityField(
    #         view_name='instauser-posts-list',
    #         lookup_url_kwarg='instauser_pk',
    #         lookup_field='pk')
    user = serializers.CharField(source='user.username')
    user_followers_count = serializers.CharField(source='followers_count')
    user_following_count = serializers.CharField(source='following_count')


    class Meta:
        model = InstaUser
        fields = ('url', 'public', 'user', 'description', 'profile_picture', 'posts', 'user_followers_count', 'user_following_count')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.HyperlinkedRelatedField(many=True, queryset=Like.objects.all(), view_name="like-detail")
    # likes = LikeSerializer(many=True)
    comments = serializers.HyperlinkedRelatedField(many=True, queryset=Comment.objects.all(), view_name="comment-detail")
    username = serializers.ReadOnlyField(source='user.user_id')

    class Meta:
        model = Post
        fields = ('url', 'username', 'date', 'value', 'description', 'likes', 'comments')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.user_id')
    post = serializers.ReadOnlyField(source='post.id')
    post_id = serializers.CharField(source='post.id')

    class Meta:
        model = Like
        fields = ('url', 'id' ,'user', 'post', 'post_id')

    def create(self, validated_data):
        return Like.objects.create(**validated_data)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.user_id')
    post = serializers.ReadOnlyField(source='post.id')
    post_id = serializers.CharField(source='post.id')

    class Meta:
        model = Comment
        fields = ('url', 'id', 'user', 'post', 'value', 'post_id')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class UserConnectionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.user_id')
    followed_user = serializers.ReadOnlyField(source='followed_user.user_id')
    followed_user_id = serializers.CharField(source='followed_user.user_id')

    class Meta:
        model = Comment
        fields = ('url', 'user', 'followed_user', 'followed_user_id')

    def create(self, validated_data):
        return UserConnection.objects.create(**validated_data)
# -------------------------------------------------
# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#         read_only=True,
#         view_name='instauser-posts-detail',
#         lookup_field='pk')
#     # user = InstaUserSerializer(required=False)
#     username = serializers.ReadOnlyField(source='user.user.username')
#
#
#     class Meta:
#         model = Post
#         fields = ('url', 'username', 'date', 'value', 'description')
#
# class InstaUserSerializer(serializers.HyperlinkedModelSerializer):
# #     posts = serializers.HyperlinkedRelatedField(many=True, queryset=Post.objects.all(),  view_name="post-detail")
# #     posts = serializers.HyperlinkedRelatedField(many=True,
# #                                                 queryset=Post.objects.all(),
# #                                                 view_name='instauser-posts-detail',
# #                                                 lookup_url_kwarg='instauser_pk')
#     posts = PostSerializer(many=True, read_only=True)
#     posts = serializers.HyperlinkedIdentityField(
#         view_name='instauser-posts-list',
#         lookup_url_kwarg='instauser_pk',
#         lookup_field='pk')
#     user = serializers.CharField(source='user.username')
#
#     class Meta:
#         model = InstaUser
#         fields = ('url', 'user', 'description', 'profile_picture', 'posts')

















