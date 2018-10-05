from django.contrib import admin
from .models import Post
# make our post visible -- login credentials
# create super user account
admin.site.register(Post)
