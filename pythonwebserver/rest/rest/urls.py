from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('quickstart/', include('quickstart.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
