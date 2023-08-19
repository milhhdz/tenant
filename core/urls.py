from django.contrib import admin
from django.urls import path

from comments.views import CreateComment

base_path = "<domain>/api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{base_path}/comments/' , CreateComment.as_view(), name='create-tenant'),
]
