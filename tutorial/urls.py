
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from snippets import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('snippets.urls')),
]
