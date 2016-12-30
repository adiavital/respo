from django.contrib import admin
from profile_user.models import InstaUser, Post , Like, Comment, UserConnection
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class InstaUserInline(admin.StackedInline):
    model = InstaUser
    can_delete = False
    verbose_name_plural = 'insta_user'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (InstaUserInline, )

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


