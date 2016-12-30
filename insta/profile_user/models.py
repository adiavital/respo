from django.db import models
from django.contrib.auth.models import User
from.user_connection_helper import user_connection_helper


class InstaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    public = models.BooleanField(max_length=100, null=False)
    description = models.CharField(max_length=3000)
    profile_picture = models.CharField(max_length=3000)

    def __str__(self):
        return self.user.username

    @property
    def followers_count(self):
        followers_count = user_connection_helper.get_user_followers_count(user_id=self.user.id)
        return followers_count

    @property
    def following_count(self):
        following_count = user_connection_helper.get_user_followings_count(user_id=self.user.id)
        return following_count


class Post(models.Model):
    user = models.ForeignKey(InstaUser, related_name='posts', on_delete=models.CASCADE)
    # date = models.DateField(auto_now_add=True)
    date = models.CharField(max_length=3000)
    value = models.CharField(max_length=3000)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.user.username) + ' post from ' + str(self.date)


class Like(models.Model):
    user = models.ForeignKey(InstaUser, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.user.username) + ' liked post from' + str(self.post.date)


class Comment(models.Model):
    user = models.ForeignKey(InstaUser, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    value = models.CharField(max_length=3000)

    def __str__(self):
        return str(self.user.user.username) + ' commented' + str(self.value)


class UserConnection(models.Model):
    user = models.ForeignKey(InstaUser, related_name='userconnections', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(InstaUser, related_name='userconnections_followed', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.user.username) + ' following' + str(self.followed_user.user.username)



