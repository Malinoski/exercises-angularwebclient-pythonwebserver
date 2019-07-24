from django.contrib import admin
from django.urls import include, path
# from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include('snippets.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('quickstart/', include('quickstart.urls')),
    path('core/', include('core.urls')),
]
